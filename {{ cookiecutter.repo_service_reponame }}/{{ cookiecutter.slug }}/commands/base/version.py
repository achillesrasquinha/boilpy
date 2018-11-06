import click

import {{ cookiecutter.slug }}

VERSION_STRING = {{ cookiecutter.slug }}.get_version_str()

@click.command(name = "version")
def version():
    """
    Show version and exit.
    """
    click.echo(VERSION_STRING)