<div align="center">
    <h1>
        {{ cookiecutter.name }}
    </h1>
    <h4>{{ cookiecutter.description }}</h4>
</div>

<p align="center">
    <a href="https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.github_reponame }}">
        <img src="https://img.shields.io/travis/{{ cookiecutter.github_username }}/{{ cookiecutter.github_reponame }}.svg?style=flat-square">
    </a>
    <a href="https://coveralls.io/github/{{ cookiecutter.github_username }}/{{ cookiecutter.github_reponame }}">
        <img src="https://img.shields.io/coveralls/github/{{ cookiecutter.github_username }}/{{ cookiecutter.github_reponame }}.svg?style=flat-square">
    </a>
    <a href="https://pypi.org/project/{{ cookiecutter.name.lower().replace(' ', '-') }}/">
		<img src="https://img.shields.io/pypi/v/{{ cookiecutter.name.lower().replace(' ', '-') }}.svg?style=flat-square">
	</a>
    <a href="https://pypi.org/project/{{ cookiecutter.name.lower().replace(' ', '-') }}/">
		<img src="https://img.shields.io/pypi/l/{{ cookiecutter.name.lower().replace(' ', '-') }}.svg?style=flat-square">
	</a>
</p>

### Table of Contents
* [Installation](#installation)
* [Usage](#usage)
* [License](#license)

#### Installation

```shell
$ pip install {{ cookiecutter.name.lower().replace(' ', '-') }}
```

#### Usage

#### License

This repository has been released under the [{{ cookiecutter.license }}](LICENSE).