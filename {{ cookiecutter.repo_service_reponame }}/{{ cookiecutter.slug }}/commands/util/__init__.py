from {{ cookiecutter.slug }}.util.type    import sequencify
from {{ cookiecutter.slug }}.util.imports import import_handler

def group_commands(group, commands):
    """
    Add command-paths to a click.Group
    """
    commands = sequencify(commands, type_ = tuple)

    for command in commands:
        path    = "%s.command" % command
        command = import_handler(path)
        
        group.add_command(command)
    
    return group
