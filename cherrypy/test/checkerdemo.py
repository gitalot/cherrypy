"""Demonstration app for cherrypy.checker.

This application is intentionally broken and badly designed.
To demonstrate the output of the CherryPy Checker, simply execute
this module.
"""

import os
import cherrypy
thisdir = os.path.dirname(os.path.abspath(__file__))

class Root:
    pass

if __name__ == '__main__':
    conf = {'/base': {'tools.staticdir.root': thisdir},
            # This entry should be OK.
            '/base/static': {'tools.staticdir.on': True,
                        'tools.staticdir.dir': 'static'},
            # Warn on missing folder.
            '/base/js': {'tools.staticdir.on': True,
                    'tools.staticdir.dir': 'js'},
            # Warn on dir with an abs path even though we provide root.
            '/base/static2': {'tools.staticdir.on': True,
                         'tools.staticdir.dir': '/static'},
            # Warn on dir with a relative path with no root.
            '/static3': {'tools.staticdir.on': True,
                         'tools.staticdir.dir': 'static'},
            }
    cherrypy.quickstart(Root(), config=conf)
