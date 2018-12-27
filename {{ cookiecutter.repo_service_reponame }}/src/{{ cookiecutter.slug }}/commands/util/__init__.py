from {{ cookiecutter.slug }}.util.type    import sequencify
from {{ cookiecutter.slug }}.util.imports import import_handler

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
