{% if cookiecutter.compat != "none" %}
from __future__ import absolute_import
{% endif %}

try:
    import os

    if os.environ.get("{{ cookiecutter.slug.upper() }}_JOBS_GEVENT_PATCH"):
        from gevent import monkey
        monkey.patch_all(threaded = False, select = False)
except ImportError:
    pass

# imports - module imports
from {{ cookiecutter.slug }}.__attr__ import (
    __name__,
    __version__,
{% if cookiecutter.cli == "click" %}
    __build__,
{% endif %}
{% if cookiecutter.cli != "none" %}
    __description__,
{% endif %}
    __author__
)
from {{ cookiecutter.slug }}.__main__    import main
from {{ cookiecutter.slug }}.config      import Settings
from {{ cookiecutter.slug }}.util.jobs   import run_all as run_all_jobs, run_job

settings = Settings()

{% if cookiecutter.cli != "none" %}
def get_version_str():
    version = "%s%s" % (__version__, " (%s)" % __build__ if __build__ else "")
    return version
{% endif %}