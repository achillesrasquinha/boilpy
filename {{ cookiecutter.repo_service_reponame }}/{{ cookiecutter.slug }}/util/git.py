import os
import subprocess

def get_revision(path, raise_err = True):
    """
    """
    revision = None

    try:
        with open(os.devnull, "w") as quiet:
            output   = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd = path, stderr = quiet)
            revision = output.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        if raise_err:
            raise

    return revision