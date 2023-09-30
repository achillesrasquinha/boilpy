# imports - module imports
from upyog.cli.util     import *
from {{ cookiecutter.slug }}.cli.parser import get_args
from upyog.util._dict   import merge_dict
from upyog.util.types   import get_function_arguments

def command(fn):
    args    = get_args()
    
    params  = get_function_arguments(fn)

    params  = merge_dict(params, args)
    
    def wrapper(*args, **kwargs):
        return fn(**params)

    return wrapper