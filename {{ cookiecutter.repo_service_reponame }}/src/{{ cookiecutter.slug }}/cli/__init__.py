# imports - module imports
from {{ cookiecutter.slug }}.cli.util   import *
from {{ cookiecutter.slug }}.cli.parser import get_args
from {{ cookiecutter.slug }}.util._dict import merge_dict
from {{ cookiecutter.slug }}.util.types import get_function_arguments

def command(fn):
    args    = get_args()
    
    params  = get_function_arguments(fn)

    params  = merge_dict(params, args)
    
    def wrapper(*args, **kwargs):
        return fn(**params)

    return wrapper