import os
import subprocess

from   {{ cookiecutter.slug }}.util.system import popen
from   {{ cookiecutter.slug }}.util.string import strip

def get_revision(path, short = False, raise_err = True):
    """
    Returns the git revision of a repository. Raises error if not a valid git repository.
    """
    revision = None

    try:
        short        = "--short" if short else ""
        _, output, _ = popen("git rev-parse", short, "HEAD", cwd = path, output = False)
        revision     = output
    except (subprocess.CalledProcessError, FileNotFoundError):
        if raise_err:
            raise

    return revision