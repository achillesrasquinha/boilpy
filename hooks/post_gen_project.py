import sys, os, os.path as osp
import shutil
import subprocess

PY2 = sys.version_info.major == 2

def iteritems(dict_, **kwargs):
    if PY2:
        iterator = dict_.iteritems()
    else:
        iterator = iter(dict_.items(), **kwargs)
    return iterator

def remove(*paths, recursive = False, raise_err = True):
    for path in paths:
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

def popen(*args, **kwargs):
    output      = kwargs.get("output", True)
    directory   = kwargs.get("cwd")
    environment = kwargs.get("env")
    shell       = kwargs.get("shell", True)
    raise_err   = kwargs.get("raise_err", True)

    environ     = os.environ.copy()
    if environment:
        environ.update(environment)

    for k, v in iteritems(environ):
        environ[k] = str(v)

    command     = " ".join([str(arg) for arg in args])
    
    proc        = subprocess.Popen(command,
        stdin   = None if output else subprocess.PIPE,
        stdout  = None if output else subprocess.PIPE,
        stderr  = None if output else subprocess.PIPE,
        env     = environ,
        cwd     = directory,
        shell   = shell
    )

    code        = proc.wait()

    if code and raise_err:
        raise subprocess.CalledProcessError(code, command)

    if output:
        output, error = proc.communicate()

        if output:
            output = output.decode("utf-8")

        if error:
            error  = error.decode("utf-8")

        return code, output, error
    else:
        return code

def setup_git_repo(path, remote = None, commit = False):
    popen("git init", cwd = path, output = False)

    if remote:
        popen("git remote add origin", remote,  cwd = path, output = False)

    if commit:
        popen("git add .")
        popen("git commit -m 'Initial Commit'", cwd = path, output = False)

        popen("git checkout -B develop --track master", cwd = path, output = False)
        popen("git checkout -B hotfix  --track master", cwd = path, output = False)
        popen("git checkout master", cwd = path, output = False)

BASEDIR = osp.realpath(osp.curdir)
SRCDIR  = osp.join(BASEDIR, "src")
TESTDIR = osp.join(BASEDIR, "tests")
PROJDIR = osp.join(SRCDIR,  "{{ cookiecutter.slug }}")

if __name__ == "__main__":
    if "{{ cookiecutter.license }}" == "none":
        remove(osp.join(BASEDIR, "LICENSE"))

    if "{{ cookiecutter.cli }}"     != "click":
        remove(
            osp.join(PROJDIR, "util", "imports.py"),
            osp.join(PROJDIR, "util", "type.py"),
            osp.join(TESTDIR, "util", "test_imports.py"),
            osp.join(TESTDIR, "util", "test_type.py")
        )
        
    if "{{ cookiecutter.cli }}"     != "argparse":
        remove(osp.join(PROJDIR, "cli"), recursive = True)

    if "{{ cookiecutter.cli }}"     == "none":
        remove(
            osp.join(PROJDIR, "__main__.py"),
            osp.join(PROJDIR, "commands"),
            osp.join(PROJDIR, "util"),
            osp.join(TESTDIR, "commands"),
            osp.join(TESTDIR, "util")
        , recursive = True)

    if "{{ cookiecutter.compat }}"  != "custom":
        remove(
            osp.join(PROJDIR, "_compat.py"),
            osp.join(TESTDIR, "test__compat.py")
        )

    if "{{ cookiecutter.compat }}"  == "none":
        remove(osp.join(BASEDIR, "requirements", "compatibility.txt"))
    
    if "{{ cookiecutter.config }}" != "y":
        remove(
            osp.join(PROJDIR, "cache.py")
        )

    if "github" not in "{{ cookiecutter.repo_service }}":
        remove(osp.join(BASEDIR, ".github"), recursive = True)

    if "gitlab" not in "{{ cookiecutter.repo_service }}":
        remove(
            osp.join(BASEDIR, ".gitlab"),
            osp.join(BASEDIR, ".gitlab-ci.yml")
        , recursive = True)

    if "{{ cookiecutter.editor }}" == "other":
        remove(osp.join(BASEDIR, ".vscode"), recursive = True)

    remote = "/".join([
        "{{ cookiecutter.repo_service }}",
        "{{ cookiecutter.repo_service_username }}",
        "{{ cookiecutter.repo_service_reponame }}"
    ])
    setup_git_repo(BASEDIR, remote = remote, commit = True)