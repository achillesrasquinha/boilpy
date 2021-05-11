<div align="center">
    <h1>
        {{ cookiecutter.name }}
    </h1>
    <h4>{{ cookiecutter.description }}</h4>
</div>

<p align="center">
    <a href="https://travis-ci.org/{{ cookiecutter.repo_service_username }}/{{ cookiecutter.repo_service_reponame }}">
      <img src="https://img.shields.io/travis/{{ cookiecutter.repo_service_username }}/{{ cookiecutter.repo_service_reponame }}.svg?style=flat-square">
    </a>
    <a href="https://coveralls.io/github/{{ cookiecutter.repo_service_username }}/{{ cookiecutter.repo_service_reponame }}">
      <img src="https://img.shields.io/coveralls/github/{{ cookiecutter.repo_service_username }}/{{ cookiecutter.repo_service_reponame }}.svg?style=flat-square">
    </a>
    <a href="https://pypi.org/project/{{ cookiecutter.name.lower().replace(' ', '-') }}/">
      <img src="https://img.shields.io/pypi/v/{{ cookiecutter.name.lower().replace(' ', '-') }}.svg?style=flat-square">
    </a>
    <a href="https://pypi.org/project/{{ cookiecutter.name.lower().replace(' ', '-') }}/">
      <img src="https://img.shields.io/pypi/l/{{ cookiecutter.name.lower().replace(' ', '-') }}.svg?style=flat-square">
    </a>
    <a href="https://pypi.org/project/{{ cookiecutter.name.lower().replace(' ', '-') }}/">
		  <img src="https://img.shields.io/pypi/pyversions/{{ cookiecutter.name.lower().replace(' ', '-') }}.svg?style=flat-square">
	  </a>
    <a href="https://git.io/boilpy">
      <img src="https://img.shields.io/badge/made%20with-boilpy-red.svg?style=flat-square">
    </a>
</p>

### Table of Contents
* [Features](#features)
* [Installation](#installation)
* [Usage](#usage)
* [License](#license)

#### Features


#### Installation

```shell
$ pip install {{ cookiecutter.name.lower().replace(' ', '-') }}
```

#### Usage

##### Application Interface

```python
>>> import {{ cookiecutter.slug }}
```

{% if cookiecutter.cli != "none" %}
##### Command-Line Interface

```console
$ {{ cookiecutter.command }}
Usage: {{ cookiecutter.command }} [OPTIONS] COMMAND [ARGS]...

  {{ cookiecutter.description }}

Options:
  --version   Show the version and exit.
  -h, --help  Show this message and exit.

Commands:
  help     Show this message and exit.
  version  Show version and exit.
```
{% endif %}

#### License

This repository has been released under the [{{ cookiecutter.license }}](LICENSE).

---

<div align="center">
  Made with ❤️ using <a href="https://git.io/boilpy">boilpy</a>.
</div>