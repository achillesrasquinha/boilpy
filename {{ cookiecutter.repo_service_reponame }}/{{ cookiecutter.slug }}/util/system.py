{% if   cookiecutter.compat == "six" %}
from six import iteritems
{% elif cookiecutter.compat == "custom" %}
from {{ cookiecutter.slug }}._compat import iteritems
{% endif %}

import os, os.path as osp
import subprocess

from   {{ cookiecutter.slug }}.util.string import strip

def read(path):
    content = None

    with open(path) as f:
        content = f.read()

    return content    

def pardir(path, level = 1):
    for _ in range(level):
        path = osp.dirname(path)
    return path

def popen(*args, **kwargs):
    output      = kwargs.get("output", True)
    directory   = kwargs.get("cwd")
    environment = kwargs.get("env")
    shell       = kwargs.get("shell", True)
    raise_err   = kwargs.get("raise_err", True)

    environ     = os.environ.copy()
    if environment:
        environ.update(environment)

    for k, v in {% if cookiecutter.compat != "none" %}iteritems(environ){% else %}environ.items(){% endif %}:
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

    if not output:
        output, error = proc.communicate()

        if output:
            output = output.decode("utf-8")
            output = strip(output)

        if error:
            error  = error.decode("utf-8")
            error  = strip(error)

        return code, output, error
    else:
        return code