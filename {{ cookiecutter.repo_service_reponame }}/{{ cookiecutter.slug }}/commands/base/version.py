import click

import {{ cookiecutter.slug }}

VERSION_STRING = {{ cookiecutter.slug }}.get_version_str()

@click.command(name = "version")
def command(ctx):
    """
    Show version and exit.
    """
    version = VERSION_STRING
    click.echo(version)