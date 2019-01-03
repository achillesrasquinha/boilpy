# pylint: disable=E0602

import sys
import os.path as osp

from   setuptools import setup, find_packages

import pip

try:
    from pip._internal.req import parse_requirements # pip 10
except ImportError:
    from pip.req           import parse_requirements # pip 9

# globals
PACKAGE     = "{{ cookiecutter.slug }}"
SRCDIR      = "src"

def isdef(var):
    return var in globals()

def read(path):
    content = None
    
    with open(path) as f:
        content = f.read()

    return content

def get_package_info():
    attr = osp.join(SRCDIR, PACKAGE, "__attr__.py")
    info = dict(__file__ = attr) # HACK
    
    with open(attr) as f:
        content = f.read()
        exec(content, info)

    return info

def get_dependencies(type_ = None):
    path         = osp.abspath("requirements{type_}.txt".format(
        type_    = "-dev" if type_ == "development" else ""
    ))
    requirements = [str(ir.req) for ir in parse_requirements(path, session = "hack")]
    
    return requirements

PKGINFO    = get_package_info()

setup(
    name                 = PKGINFO["__name__"],
    version              = PKGINFO["__version__"],
    url                  = PKGINFO["__url__"],
    author               = PKGINFO["__author__"],
    author_email         = PKGINFO["__email__"],
    description          = PKGINFO["__description__"],
    long_description     = read("README.md"),
    license              = PKGINFO["__license__"],
    keywords             = " ".join(PKGINFO["__keywords__"]),
    packages             = find_packages(where = SRCDIR),
    package_dir          = { "": SRCDIR },
    zip_safe             = False,
    {% if cookiecutter.cli != "none" %}
    entry_points         = {
        "console_scripts": [
            "%s = %s.__main__:main" % (
                PKGINFO["__command__"] if hasattr(PKGINFO, "__command__") else PKGINFO["__name__"],
                PACKAGE
            )
        ]
    },
    {% endif %}
    install_requires     = get_dependencies(type_ = "production"),
    extras_require       = dict(
        dev = get_dependencies(type_ = "development")
    ),
    include_package_data = True,
    classifiers          = (
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        {% if cookiecutter.compat != "none" %}
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        {% endif %}
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy"
    )
)