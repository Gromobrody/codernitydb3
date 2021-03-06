import functools
from collections import Counter, defaultdict
from heapq import nsmallest
from operator import itemgetter


def cache1lvl(maxsize=100):
    """
    modified version of http://code.activestate.com/recipes/498245/
    """

    def decorating_function(user_function):
        cache = {}
        use_count = Counter()

        @functools.wraps(user_function)
        def wrapper(key, *args, **kwargs):
            try:
                result = cache[key]
            except KeyError:
                if len(cache) == maxsize:
                    for k, _ in nsmallest(
                        maxsize // 10 or 1, use_count.items(), key=itemgetter(1)
                    ):
                        del cache[k], use_count[k]
                cache[key] = user_function(key, *args, **kwargs)
                result = cache[key]
                # result = user_function(obj, key, *args, **kwargs)
            finally:
                use_count[key] += 1
            return result

        def clear():
            cache.clear()
            use_count.clear()

        def delete(key):
            try:
                del cache[key]
                del use_count[key]
            except KeyError:
                return False
            else:
                return True

        wrapper.clear = clear
        wrapper.cache = cache
        wrapper.delete = delete
        return wrapper

    return decorating_function


def twolvl_iterator(d):
    for k, v in d.items():
        for kk, vv in v.items():
            yield k, kk, vv


def cache2lvl(maxsize=100):
    """
    modified version of http://code.activestate.com/recipes/498245/
    """

    def decorating_function(user_function):
        cache = {}
        use_count = defaultdict(Counter)

        @functools.wraps(user_function)
        def wrapper(*args, **kwargs):
            #            return user_function(*args, **kwargs)
            try:
                result = cache[args[0]][args[1]]
            except KeyError:
                if wrapper.cache_size == maxsize:
                    to_delete = maxsize // 10 or 1
                    for k1, k2, v in nsmallest(
                        to_delete, twolvl_iterator(use_count), key=itemgetter(2)
                    ):
                        del cache[k1][k2], use_count[k1][k2]
                        if not cache[k1]:
                            del cache[k1]
                            del use_count[k1]
                    wrapper.cache_size -= to_delete
                result = user_function(*args, **kwargs)
                try:
                    cache[args[0]][args[1]] = result
                except KeyError:
                    cache[args[0]] = {args[1]: result}
                wrapper.cache_size += 1
            finally:
                use_count[args[0]][args[1]] += 1
            return result

        def clear():
            cache.clear()
            use_count.clear()

        def delete(key, inner_key=None):
            if inner_key is not None:
                try:
                    del cache[key][inner_key]
                    del use_count[key][inner_key]
                    if not cache[key]:
                        del cache[key]
                        del use_count[key]
                    wrapper.cache_size -= 1
                except KeyError:
                    return False
                else:
                    return True
            else:
                try:
                    wrapper.cache_size -= len(cache[key])
                    del cache[key]
                    del use_count[key]
                except KeyError:
                    return False
                else:
                    return True

        wrapper.clear = clear
        wrapper.cache = cache
        wrapper.delete = delete
        wrapper.cache_size = 0
        return wrapper

    return decorating_function
