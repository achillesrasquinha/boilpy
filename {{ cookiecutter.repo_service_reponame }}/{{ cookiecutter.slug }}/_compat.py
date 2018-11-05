import sys

PY2 = sys.version_info.major == 2

if PY2:
    {% if cookiecutter.cli == "argparse" %}
    from __builtin__ import raw_input as input
    {% else %}
    pass
    # Add your Python 2 imports here.
    {% endif %}
else:
    {% if cookiecutter.cli == "argparse" %}
    from builtins import input
    {% else %}
    pass
    # Add your Python 3 imports here.
    {% endif %}