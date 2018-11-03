import click
import click_completion
from   click_didyoumean import DYMGroup

from   {{ cookiecutter.slug }}.commands.util import group_commands
import {{ cookiecutter.slug }}

click_completion.init()

# default context settings
CONTEXT_SETTINGS = dict(
    help_option_names = ["-h", "--help"]
)
VERSION_STRING   = "%s%s" % ({{ cookiecutter.slug }}.__version__, " (%s)" % {{ cookiecutter.slug }}.__build__ if {{ cookiecutter.slug }}.__build__ else "")

@click.group(
    name = {{ cookiecutter.slug }}.__name__,
    cls  = DYMGroup,
    help = {{ cookiecutter.slug }}.__description__,
    context_settings = CONTEXT_SETTINGS
)
@click.version_option(
    version = VERSION_STRING,
    message = "%(version)s"
)
def group():
    pass

command = group_commands(group, (
    "{{ cookiecutter.slug }}.commands.base.help"
))

def main():
    code = command(prog_name = {{ cookiecutter.slug }}.__name__, obj = {}) # pylint: disable=E1111,E1123,E1120
    return code