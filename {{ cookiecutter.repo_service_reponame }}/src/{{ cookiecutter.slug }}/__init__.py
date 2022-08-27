{% if cookiecutter.compat != "none" %}
from __future__ import absolute_import
{% endif %}

try:
    import os

    if os.environ.get("{{ cookiecutter.slug.upper() }}_GEVENT_PATCH"):
        from gevent import monkey
        monkey.patch_all(threaded = False, select = False)
except ImportError:
    pass

# imports - module imports
from {{ cookiecutter.slug }}.__attr__ import (
    __name__,
    __version__,
    __build__,
{% if cookiecutter.cli != "none" %}
    __description__,
{% endif %}
    __author__
)
from {{ cookiecutter.slug }}.config      import PATH
from {{ cookiecutter.slug }}.__main__    import main
{% if cookiecutter.api == "y" %}
from {{ cookiecutter.slug }}.api.client  import Client
{% endif %}
from bpyutils.cache       import Cache
from bpyutils.config      import Settings
from bpyutils.util.jobs   import run_all as run_all_jobs, run_job


cache = Cache(dirname = __name__)
cache.create()

settings = Settings()

{% if cookiecutter.cli != "none" %}
def get_version_str():
    version = "%s%s" % (__version__, " (%s)" % __build__ if __build__ else "")
    return version
{% endif %}

{% if cookiecutter.ml == "y" %}
import deeply

dops = deeply.ops.service("wandb")
dops.init("{{ cookiecutter.slug }}")
{% endif %}