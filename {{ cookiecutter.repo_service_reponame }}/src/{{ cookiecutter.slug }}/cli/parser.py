# imports - module imports
from {{ cookiecutter.slug }}.__attr__     import (
    __name__,
    __version__,
    __description__,
    __command__
)
from upyog.cli             import util as _cli
from upyog.cli.parser      import get_base_parser

_DESCRIPTION_JUMBOTRON = \
"""
%s (v %s)

%s
""" % (
    _cli.format(__name__,        _cli.RED),
    _cli.format(__version__,     _cli.BOLD),
    _cli.format(__description__, _cli.BOLD)
)

def get_parser():
    parser = get_base_parser(__command__, _DESCRIPTION_JUMBOTRON)
    return parser

def get_args(args = None, known = True, as_dict = True):
    parser  = get_parser()

    if known:
        args, _ = parser.parse_known_args(args)
    else:
        args    = parser.parse_args(args)

    if as_dict:
        args = args.__dict__
        
    return args