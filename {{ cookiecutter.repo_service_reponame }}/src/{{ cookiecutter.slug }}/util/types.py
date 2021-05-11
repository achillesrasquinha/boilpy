# pylint: disable=E1101

# imports - compatibility imports
from pipupgrade             import _compat
from pipupgrade._compat     import zip, _is_python_version
from pipupgrade.util._dict  import dict_from_list

# imports - standard imports
import sys
import inspect
import collections
import itertools

def get_function_arguments(fn):
    # https://stackoverflow.com/a/2677263
    params  = dict()
    success = False
    
    if _compat.PY2: # pragma: no cover
        argspec_getter = inspect.getargspec
        success        = True
    if _compat.PYTHON_VERSION >= (3,0) and _compat.PYTHON_VERSION < (3,5): # pragma: no cover
        argspec_getter = inspect.getfullargspec
        success        = True

    if success: # pragma: no cover
        argspec   = argspec_getter(fn)
        params    = dict_from_list(argspec.args, argspec.defaults or [])

    if _compat.PYTHON_VERSION >= (3,5):
        signature  = inspect.signature(fn)
        parameters = signature.parameters

        params     = { k: v.default for k, v in _compat.iteritems(parameters) }

        success    = True

    if not success: # pragma: no cover
        raise ValueError("Unknown Python Version {} for fetching functional arguments.".format(sys.version))

    return params

def auto_typecast(value):
    str_to_bool = lambda x: { "True": True, "False": False, "None": None}[x]

    for type_ in (str_to_bool, int, float):
        try:
            return type_(value)
        except (KeyError, ValueError, TypeError):
            pass

    return value