import click

@click.command(name = "config")
@click.argument("key")
@click.argument("value")
def config():
    """
    Set Config.
    """
    {{ cookiecutter.slug }}.cache.config[key] = value