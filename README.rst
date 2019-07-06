App Store: User-Oriented Front-End for PIP
==========================================

`App Store`_ is an Apache2 licensed, user-oriented front-end for ``pip``,
written in pure-Python, and compatible with Windows, Mac OS X, and Linux.

`App Store`_ is currently in the planning stages. But your thoughts and help
are welcome.

Background
----------

I feel I see a lot of folks complain about Python packaging and distribution
online. Recently, `PyOxidizer`_ was published as yet another solution in this
space. Personally, I have always found either `PyInstaller`_ or Cython's
`embed`_ option to be sufficient. But I really think these tools are solving
the wrong problem.

Most of the tooling is meant to produce a binary executable. But that's kind of
the easy part. The hard part is updates, crash reports, and uninstalls. It's
managing the whole lifecycle of an application.

When I worked at Microsoft, I used a `ClickOnce`_ application and my experience
was ideal. Installation and updates just worked seemlessly. I clicked the
installer once and everything just worked. It was like installing an app on my
phone and running it. I don't know how any of that works, but it just works.

Recently, I developed a Python package with a few requirements and a few static
files. It was just a bit more than a single script could manage. My go-to for
internal business needs in that case is a locally hosted PyPI or simple wheel
file. I wanted that to work here too but I didn't want to teach ``pip`` and
``venv`` to run my script. What I wanted was a pip-porcelain.

I think a graphical PIP could go a bit further and be an app store for Python
packages. I love the idea of running Python scripts or pyc files easily on the
client machine. I don't even care if it's just a command-line application. Give
me something that handles installs, updates, uninstalls, and crash reports and
I'll be happy. And allow me to continue using ``__file__`` and writing
cross-platform Python scripts that don't require separate compilation.

I imagine something like a webserver running on the client's machine with an
icon in the taskbar. Let's use "A" as our icon for now. Click the icon and a
webbrowser opens pointing to localhost with a gui front-end for PIP. I think
`rumps`_ would get us there on Macs. Win32 must have something similar and
Ubuntu or whatnot something too. For deployment, use `fbs`_.

`App Store`_ is currently in the planning stages. But your thoughts and help
are welcome.

.. _`PyOxidizer`: https://github.com/indygreg/PyOxidizer
.. _`PyInstaller`: https://www.pyinstaller.org/
.. _`embed`: https://github.com/cython/cython/wiki/EmbeddingCython
.. _`ClickOnce`: https://docs.microsoft.com/en-us/visualstudio/deployment/clickonce-security-and-deployment
.. _`rumps`: https://github.com/jaredks/rumps
.. _`fbs`: https://build-system.fman.io/

Features
--------

- Pure-Python
- *TODO* Fully Documented
- *TODO* 100% Test Coverage
- *TODO* One-Click Executables for Windows, Mac OS X, and Linux
- *TODO* Graphical User Interface for ``pip``
- *TODO* Package Installs, Updates, Uninstalls
- *TODO* ``venv``'s for Installed Packages
- *TODO* Crash Reports
- *TODO* Startup Utilities: Windows Start Menu, Mac OS X Applications Folder
- Developed on Python 3.7
- Tested on CPython 2.7, 3.5, 3.6, and 3.7
- Tested on Linux, Mac OS X, and Windows
- Tested using Travis CI and AppVeyor CI

.. image:: https://api.travis-ci.org/grantjenks/python-appstore.svg?branch=master
    :target: http://www.grantjenks.com/docs/appstore/

.. image:: https://ci.appveyor.com/api/projects/status/github/grantjenks/python-appstore?branch=master&svg=true
    :target: http://www.grantjenks.com/docs/appstore/

Quickstart
----------

Installing `App Store`_ is simple with `pip <http://www.pip-installer.org/>`_::

    $ pip install appstore

You can access documentation in the interpreter with Python's built-in help
function::

    >>> import appstore
    >>> help(appstore)

User Guide
----------

For those wanting more details, this part of the documentation describes
tutorial, benchmarks, API, and development.

* `App Store Tutorial`_
* `App Store API Reference`_

.. _`App Store Tutorial`: http://www.grantjenks.com/docs/appstore/tutorial.html
.. _`App Store API Reference`: http://www.grantjenks.com/docs/appstore/api.html

Reference
---------

* `App Store Documentation`_
* `App Store at PyPI`_
* `App Store at GitHub`_
* `App Store Issue Tracker`_

.. _`App Store Documentation`: http://www.grantjenks.com/docs/appstore/
.. _`App Store at PyPI`: https://pypi.python.org/pypi/appstore/
.. _`App Store at GitHub`: https://github.com/grantjenks/python-appstore/
.. _`App Store Issue Tracker`: https://github.com/grantjenks/python-appstore/issues/

License
-------

Copyright 2019 Grant Jenks

Licensed under the Apache License, Version 2.0 (the "License"); you may not use
this file except in compliance with the License.  You may obtain a copy of the
License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed
under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
CONDITIONS OF ANY KIND, either express or implied.  See the License for the
specific language governing permissions and limitations under the License.

.. _`App Store`: http://www.grantjenks.com/docs/appstore/
