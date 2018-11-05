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


#### License

This repository has been released under the [{{ cookiecutter.license }}](LICENSE).