.. _install:

### Installation

#### Installation via pip

The recommended way to install **{{ cookiecutter.name }}** is via `pip`.

```shell
$ pip install {{ cookiecutter.name.lower().replace(' ', '-') }}
```

For instructions on installing python and pip see “The Hitchhiker’s Guide to Python” 
[Installation Guides](https://docs.python-guide.org/starting/installation/).

#### Building from source

`{{ cookiecutter.name.lower().replace(' ', '-') }}` is actively developed on [{{ cookiecutter.repo_service }}]({{ cookiecutter.repo_service }}/{{ cookiecutter.repo_service_username }}/{{ cookiecutter.repo_service_reponame }})
and is always avaliable.

You can clone the base repository with git as follows:

```shell
$ git clone {{ cookiecutter.repo_service }}/{{ cookiecutter.repo_service_username }}/{{ cookiecutter.repo_service_reponame }}
```

Optionally, you could download the tarball or zipball as follows:

##### For Linux Users

```shell
$ curl -OL {{ cookiecutter.repo_service }}/{{ cookiecutter.repo_service_username }}/tarball/{{ cookiecutter.repo_service_reponame }}
```

##### For Windows Users

```shell
$ curl -OL {{ cookiecutter.repo_service }}/{{ cookiecutter.repo_service_username }}/zipball/{{ cookiecutter.repo_service_reponame }}
```

Install necessary dependencies

```shell
$ cd {{ cookiecutter.repo_service_reponame }}
$ pip install -r requirements.txt
```

Then, go ahead and install {{ cookiecutter.name }} in your site-packages as follows:

```shell
$ python setup.py install
```

Check to see if you’ve installed {{ cookiecutter.name }} correctly.

```shell
$ {{ cookiecutter.command }} --help
```