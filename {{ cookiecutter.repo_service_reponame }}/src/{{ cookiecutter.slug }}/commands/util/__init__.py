{% if cookiecutter.cli == "click" %}
from upyog.util.array   import sequencify
from upyog.util.imports import import_handler
{% endif %}

# imports - module imports
from {{ cookiecutter.slug }}.cli.parser import get_args
from {{ cookiecutter.slug }} import cli

{% if cookiecutter.cli == "click" %}
def group_commands(group, commands):
    """
    Add command-paths to a click.Group
    """
    commands = sequencify(commands, type_ = tuple)

    for command in commands:
        head, tail = command.rsplit(".", 1)
        tails      = ("", tail, "command")

        for i, tail in enumerate(tails):
            try:
                path    = "%s.%s" % (command, tail)
                command = import_handler(path)

                break
            except:
                if i == len(tails) - 1:
                    raise
        
        group.add_command(command)
    
    return group
{% endif %}

def cli_format(string, type_):
    args = get_args(as_dict = False)
    
    if hasattr(args, "no_color") and not args.no_color:
        string = cli.format(string, type_)

    return string