App Store Tutorial
==================

.. contents::
   :depth: 1
   :local:

Installation
------------

This part of the documentation covers the installation of :doc:`App Store
<index>`. The first step to using any software package is getting it properly
installed.

Pip & PyPI
..........

Installing :doc:`App Store <index>` is simple with `pip
<https://pip.pypa.io/en/stable/>`_::

    $ pip install --upgrade appstore

The versioning scheme uses `major.minor.micro` with `micro` intended for bug
fixes, `minor` intended for small features or improvements, and `major`
intended for significant new features and breaking changes. While it is
intended that only `major` version changes are backwards incompatible, it is
not always guaranteed. When running in production, it is recommended to pin at
least the `major` version.

Get the Code
............

:doc:`App Store <index>` is actively developed on GitHub, where the code is
always available.

You can either clone the `App Store repository <https://github.com/grantjenks/python-appstore>`_::

    $ git clone https://github.com/grantjenks/python-appstore.git

Once you have a copy of the source, you can embed it in your Python package,
or install it into your site-packages easily::

    $ python setup.py install

:doc:`App Store <index>` is looking for a Debian package maintainer. If you can
help, please open an issue in the `App Store Issue Tracker`_.

:doc:`App Store <index>` is looking for a CentOS/RPM package maintainer.  If
you can help, please open an issue in the `App Store Issue Tracker`_.

.. _`App Store Issue Tracker`: https://github.com/grantjenks/python-appstore/issues/

App Store
---------

.. todo::

   Tutorial for using App Store.
