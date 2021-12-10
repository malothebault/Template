#!/usr/bin/python3

from distutils.core import setup

'''Here we are defining where should be placed each file'''
install_data = [
    ('share/applications', ['data/com.github.malothebault.escapade.desktop']),
    ('share/metainfo', ['data/com.github.malothebault.escapade.appdata.xml']),
    ('share/icons/hicolor/128x128/apps', ['data/com.github.malothebault.escapade.svg']),
    ('/usr/share/glib-2.0/schemas', ["data/com.github.malothebault.escapade.gschema.xml"]),
    ('bin/escapade', ['src/brackets.py']),
    ('bin/escapade', ['src/constants.py']),
    ('bin/escapade', ['src/handler.py']),
    ('bin/escapade', ['src/headerbar.py']),
    ('bin/escapade', ['src/initialisation.py']),
    ('bin/escapade', ['src/listofname.py']),
    ('bin/escapade', ['src/main.py']),
    ('bin/escapade', ['src/stack.py']),
    ('bin/escapade', ['src/teams.py']),
    ('bin/escapade', ['src/welcome.py']),
    ('bin/escapade', ['src/window.py']),
    ('bin/escapade', ['src/__init__.py']),
]

'''Let's go and infuse our application into the system.'''
setup(
    name='Escapade',
    version='0.1',
    author='Malo Thebault',
    description='Open and create GPX files. Plan your future adventure.',
    url='https://github.com/malothebault/escapade',
    license='GNU GPL3',
    scripts=['com.github.malothebault.escapade'],
    packages=['src'],
    data_files=install_data
)
