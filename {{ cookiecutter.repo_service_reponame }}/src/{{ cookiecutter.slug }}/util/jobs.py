# imports - standard imports
import os, os.path as osp
from   functools import partial
import sys

# imports - module imports
from {{ cookiecutter.slug }}.config          import PATH, Settings
from {{ cookiecutter.slug }}.util.imports    import import_handler
from {{ cookiecutter.slug }}.util.system     import popen
from {{ cookiecutter.slug }}.util._dict      import merge_dict
from {{ cookiecutter.slug }}.util.environ    import getenvvar, getenv
from {{ cookiecutter.slug }} import parallel, log

settings = Settings()
logger   = log.get_logger()

JOBS = [
    
]

def run_job(name, variables = None):
    job = [job for job in JOBS if job["name"] == name]
    if not job:
        raise ValueError("No job %s found." % name)
    else:
        job = job[0]

    variables = merge_dict(job.get("variables", {}), variables or {})

    popen("%s -c 'from {{ cookiecutter.slug }}.util.imports import import_handler; import_handler(\"%s\")()'" %
        (sys.executable, "{{ cookiecutter.slug }}.jobs.%s.run" % name), env = variables)

def run_all():
    logger.info("Running all jobs...")
    for job in JOBS:
        if not job.get("beta") or getenv("JOBS_BETA"):
            run_job(job["name"], variables = job.get("variables"))