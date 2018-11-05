import os, os.path as osp
import shutil

def remove(path, recursive = False, raise_err = True):
    path = osp.abspath(path)

    if osp.isdir(path):
        if recursive:
            shutil.rmtree(path)
        else:
            if raise_err:
                raise OSError("{path} is a directory.".format(
                    path = path
                ))
    else:
        try:
            os.remove(path)
        except OSError:
            if raise_err:
                raise

BASEDIR = osp.realpath(osp.curdir)
PROJDIR = osp.join(BASEDIR, "{{ cookiecutter.slug }}")

if __name__ == "__main__":
    if "{{ cookiecutter.license }}" == "none":
        remove(osp.join(BASEDIR, "LICENSE"))

    if "{{ cookiecutter.cli }}"     != "argparse":
        remove(osp.join(PROJDIR, "cli"), recursive = True)

    if "{{ cookiecutter.compat }}"  != "custom":
        remove(osp.join(PROJDIR, "_compat.py"))

    if "github" not in "{{ cookiecutter.repo_service }}":
        remove(osp.join(BASEDIR, ".github"), recursive = True)

    if "gitlab" not in "{{ cookiecutter.repo_service }}":
        remove(osp.join(BASEDIR, ".gitlab"), recursive = True)