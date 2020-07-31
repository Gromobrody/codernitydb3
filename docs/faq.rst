.. _faq:

====================
FAQ
====================


Here you will find some questions and answers


Is it production ready ?
    We already use it in several projects. Even currently we care about backwards compatible changes. It's **ready for production use**.

What about JOINs (known from SQL databases) ?
    You can write database function. Please see :ref:`join_like1`. Just remember codernitydb3 is *not* relational database.

Will it work on Jython ?
    On 2.5 no, on 2.7 it will work pretty fine.

How fast is codernitydb3 ?
    It's pretty fast. It can be said that you can insert even more than 55 000 records to Hash Index every second (see :ref:`speed` for more details)

Can I add index to existing DB ?
    Yes you can, but you will need to reindex that index to have in it data that were in database already before you add that index. (see :ref:`database_indexes` for details)

Can I do prefix/infix/suffix search in codernitydb3 ?
    Sure! Please refer to :ref:`multiple_keys_index`. By using such method you will get very fast prefix/infix/suffix search mechanism.

What about tables or collections ?
    Everything can be done through our Index mechanism see :ref:`tables_collections_q`.

How does it compare to MongoDB, CouchDB and other "big" NoSQL databases ?
    Different purposes + different design. codernitydb3 doesn't have yet any replication engine (yet?). However we are sure that there is a place for codernitydb3. Nothing is impossible in codernitydb3, because Index IS a Python class where you can do anything (if you're not a Python user we created :ref:`simple_index`). Don't try make codernitydb3 relational database, it will work but its not *that*. It can act as a simple key-value database or as a database with secondary indexes (ordering / selecting etc). You can optimize IO performance by moving indexes data on different partitions. Generally the codernitydb3 index mechanism is really powerful, its much more than in other databases (it's more similar to CouchDB views). Index is python class, so the sky is the limit.

How does it compare to Redis, Kyoto Cabinet and other Key/Value databases ?
    First of all it has to be said, codernitydb3 is **NOT** typical Key/Value database. It's much more. codernitydb3 has support for multiple indexes, can perform range queries, it can index more than one value per incoming record. It's much more than typical Key/Value database. And codernitydb3 index is a python class, so the sky is the limit there. Please keep in mind that you can easily embed codernitydb3 (which you can't do with Redis)

Is it daybreak (Ruby Simple Key/Value database) but for Python ?
    Not really, codernitydb3 is much more. codernitydb3 always store Python dict type as data value. codernitydb3 has multiple index support, it can use TreeIndex and HashIndex. codernitydb3 can work as daybreak but by default it's designed to be something more than "simple key/value". They are generally as you can see not the same things.

Why Python 3 is not supported ?
    Python 3 introduced many incompatible changes. In case of codernitydb3 having working version for 2.x and 3.x series in the same code base without ugly hacks (big monkey-patching etc.) is almost impossible. If you're interested Python 3 version of codernitydb3 contact us. Porting codernitydb3 to Python 3.x is not hard. Python 3.x support in fact was never needed. That's why there is no support for it (yet?).

I want to contribute, what can I do?
    Just fork and create pull request |bitbucket_link|.

I found a bug, where can I report it?
    Please report it on Bitbucket bugtracker in our repo |bitbucket_link|.

I want to have a bit customized codernitydb3
    No problem, just contact us to get more details about that.

What If I want to implement my own Index ?
    At first you have to remember that implementing custom index shouldn't require changes in Database itself. Because of codernitydb3 design, database object tries to perform operations on particular index as fast as it's possible. Good example of such method is :ref:`multiple_keys_index`.

Is there any built-in sharding mechanism ?
    Yes, there is sharding mechanism build in :ref:`sharding_in_indexes`.

I want to use codernitydb3 in commercial project, do I have to pay for it?
    codernitydb3 is released on `Apache 2.0 license`_, it allows you to freely use it even for commercial purposes without any need to pay for it.


.. _Apache 2.0 license: http://www.apache.org/licenses/LICENSE-2.0.html
