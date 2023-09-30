# imports - compatibility imports
from __future__ import absolute_import

from {{ cookiecutter.slug }}.commands.util 	import cli_format
from upyog.util._dict        import merge_dict
from upyog.util.system   	import (touch)
from upyog.util.error        import pretty_print_error
from upyog.config			import environment
from upyog.exception         import DependencyNotFoundError
from upyog import log
from {{ cookiecutter.slug }} 	import cli
from upyog._compat		    import iteritems
from {{ cookiecutter.slug }}.__attr__ import __name__

logger   = log.get_logger(level = log.DEBUG)

ARGUMENTS = dict(
    jobs						= 1,
    check		 				= False,
    interactive  				= False,
    yes			 				= False,
    no_cache		            = False,
    no_color 	 				= True,
    output						= None,
    ignore_error				= False,
    force						= False,
    verbose		 				= False
)

@cli.command
def command(**ARGUMENTS):
    try:
        return _command(**ARGUMENTS)
    except Exception as e:
        if not isinstance(e, DependencyNotFoundError):
            cli.echo()

            pretty_print_error(e)

            cli.echo(cli_format("""\
An error occured while performing the above command. This could be an issue with
"{{ cookiecutter.slug }}". Kindly post an issue at https://github.com/achillesrasquinha/{{ cookiecutter.slug }}/issues""", cli.RED))
        else:
            raise e

def to_params(kwargs):
    class O(object):
        pass

    params = O()

    kwargs = merge_dict(ARGUMENTS, kwargs)

    for k, v in iteritems(kwargs):
        setattr(params, k, v)

    return params

def _command(*args, **kwargs):
    a = to_params(kwargs)

    if not a.verbose:
        logger.setLevel(log.NOTSET)

    logger.info("Environment: %s" % environment())
    logger.info("Arguments Passed: %s" % locals())

    file_ = a.output

    if file_:
        logger.info("Writing to output file %s..." % file_)
        touch(file_)
    
    logger.info("Using %s jobs..." % a.jobs)