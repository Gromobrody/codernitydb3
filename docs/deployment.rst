Deployment
==========

To make use of graphility (or |CodernityDBPyClient-link|), you will need just to create global object that will be available to all your application threads etc.

.. seealso:

    |CodernityDBdemos| for several demo applications.


In general you *just* need to create database object and then make use of it. No special magic behind this.

Web frameworks
~~~~~~~~~~~~~~

cherrypy
    A recommended way would be CherryPy Tool

    .. literalinclude:: codes/cherrypy_tool.py
        :linenos:

    Then make use of it as normal CherryPy Tool (see: `CherryPy Custom Tools`_)

flask
    See ``minitwit`` demo in |CodernityDBdemos|


UI
~~

GTK
    See ``DesktopRSS`` demo in |CodernityDBdemos|




.. _CherryPy Custom Tools: http://docs.cherrypy.org/stable/progguide/extending/customtools.html
