# imports - compatibility imports
from upyog._compat import iteritems, iterkeys

# imports - module imports
from {{ cookiecutter.slug }} import cli
from {{ cookiecutter.slug }}.cli import get_args
from upyog.util._dict import merge_dict

def test_command():
    def _assert_command(values, override = dict(), initial = dict()):
        @cli.command
        def foobar(*args, **kwargs):
            args    = get_args()
            params  = merge_dict(args, override)
            
            for k, v in iteritems(values):
                assert params[k] == v

            if initial:
                for k in iterkeys(initial):
                    assert initial[k] == args[k]
        
        foobar()
    
    _assert_command(dict(yes = False))
    _assert_command(dict(force = True), dict(force = True), dict(force = False))