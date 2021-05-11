# imports - standard imports
import subprocess as sp

class {{ cookiecutter.slug.capitalize() }}Error(Exception):
    pass

class PopenError({{ cookiecutter.slug.capitalize() }}Error, sp.CalledProcessError):
    pass

class DependencyNotFoundError(ImportError):
    pass