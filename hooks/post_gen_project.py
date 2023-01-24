import os, os.path as osp

from bpyutils.util.system   import remove, popen
from bpyutils.util.environ  import getenv
from bpyutils.util.git      import setup_git_repo
from bpyutils.api.github    import GitHub

GIT_USERNAME = "boilpy bot"
GIT_EMAIL    = "achillesrasquinha@gmail.com"

BASEDIR = osp.realpath(osp.curdir)
SRCDIR  = osp.join(BASEDIR, "src")
TESTDIR = osp.join(BASEDIR, "tests", "{{ cookiecutter.slug }}")
PROJDIR = osp.join(SRCDIR,  "{{ cookiecutter.slug }}")

if __name__ == "__main__":
    if "{{ cookiecutter.license }}" == "none":
        remove(osp.join(BASEDIR, "LICENSE"))

    if "{{ cookiecutter.cli }}"     != "click":
        remove(
            osp.join(PROJDIR, "commands", "base"),
            osp.join(TESTDIR, "commands", "base")
            # osp.join(PROJDIR, "util", "imports.py"),
            # osp.join(TESTDIR, "util", "test_imports.py")
        , recursive = True)
        
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

    if "{{ cookiecutter.github_action }}" == "n":
        remove(
            osp.join(BASEDIR, "action.yml")
        )

    if "{{ cookiecutter.api }}" == "n":
        remove(
            osp.join(PROJDIR, "api"),
            osp.join(TESTDIR, "api")
        , recursive = True)

    if "{{ cookiecutter.ml }}" == "n":
        remove(
            osp.join(BASEDIR, ".github", "workflows", "model-ci.yml"),
            osp.join(PROJDIR, "data", "__init__.py"),
            osp.join(PROJDIR, "pipelines")
        , recursive = True)

    if "{{ cookiecutter.jupyter }}" == "n":
        remove(
            osp.join(BASEDIR, "docs", "notebooks")
        , recursive = True, raise_err = False)

    remote = "/".join([
        "{{ cookiecutter.repo_service }}",
        "{{ cookiecutter.repo_service_username }}",
        "{{ cookiecutter.repo_service_reponame }}"
    ])

    popen("make requirements", cwd = BASEDIR, output = False)

    os.rename(osp.join(BASEDIR, ".env-template"), ".env")

    if "{{ cookiecutter.ros }}" == "n":
        remove(
            osp.join(BASEDIR, "CMakeLists.txt"),
            osp.join(BASEDIR, "package.xml"),
            osp.join(BASEDIR, "launch"),
            osp.join(BASEDIR, "msg")
        , recursive = True, raise_err = False)

    token = getenv("GITHUB_TOKEN", prefix = None, raise_err = False)
    if token:
        github_username = "{{ cookiecutter.repo_service_username }}"
        github_reponame = "{{ cookiecutter.repo_service_reponame }}"

        github = GitHub(token = token)
        github.repo(github_username, github_reponame, create = True,
            description = "{{ cookiecutter.description }}",
            homepage    = "{{ cookiecutter.url }}"
        )

    if not osp.exists(osp.join(BASEDIR, ".git")):
        setup_git_repo(BASEDIR, remote = remote, commit = True,
            push = True, git_username = GIT_USERNAME, git_email = GIT_EMAIL)