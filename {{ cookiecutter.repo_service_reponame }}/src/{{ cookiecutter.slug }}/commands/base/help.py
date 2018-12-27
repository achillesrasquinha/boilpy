import click

@click.command(name = "help")
@click.pass_context
def help(ctx):
    """
    Show this message and exit.
    """
    help_ = ctx.parent.get_help()
    click.echo(help_)