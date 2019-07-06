from io import open
from setuptools import setup
from setuptools.command.test import test as TestCommand

import appstore


class Tox(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True
    def run_tests(self):
        import tox
        errno = tox.cmdline(self.test_args)
        exit(errno)


with open('README.rst', encoding='utf-8') as reader:
    readme = reader.read()

setup(
    name='appstore',
    version=appstore.__version__,
    description='App Store -- user-oriented front-end for pip.',
    long_description=readme,
    author='Grant Jenks',
    author_email='contact@grantjenks.com',
    url='http://www.grantjenks.com/docs/appstore/',
    license='Apache 2.0',
    packages=['appstore'],
    tests_require=['tox'],
    cmdclass={'test': Tox},
    install_requires=[],
    classifiers=(
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
    ),
)
