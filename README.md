<!-- HEADER -->
<div align="center">
    <img src=".github/assets/logo.png" height="128"> 
    <h1>
        boilpy
    </h1>
    <h4>The Best Python Package Template in the Universe</h4>
</div>

<!-- BADGES -->
<p align="center">
	<a href="https://saythanks.io/to/achillesrasquinha">
		<img src="https://img.shields.io/badge/Say%20Thanks-🦉-1EAEDB.svg?style=flat-square">
	</a>
	<a href="https://paypal.me/achillesrasquinha">
		<img src="https://img.shields.io/badge/donate-💵-f44336.svg?style=flat-square">
	</a>
</p>

<div align="justify">
	<b>boilpy</b> is a carefully crafted Python Package Template that is designed to ease your development, testing and deployment workflow. It heavily emphasizes on <a href="https://en.wikipedia.org/wiki/Convention_over_configuration" target="_blank">convention over configuration</a> so you can focus on getting straight down to building and distributing your very next python package.
</div>

### Contents

* [Features](#features)
* [Quick Start](#quick-start)
* [Usage](#usage)
* [Documentation](docs)
* [License](#license)

### Features

* Configurable package creation with "sensible defaults".
* "Open Source First" package creation with pre-configured CI-CD.
* Industry Standard tooling capabilities.
* Python 2.7+, Python 3.4+ and PyPy aware boilerplate.

### Quick Start

<div align="center">
	<pre><a href="https://github.com/pypa/pip" target="_blank">pip</a> install -q cookiecutter && <a href="https://github.com/audreyr/cookiecutter" target="_blank">cookiecutter</a> https://github.com/achillesrasquinha/boilpy</pre>
</div>

For an exhaustive installation guide, you can visit the Documentation [here](docs/installation.md).

### Usage

**boilpy** provides you a production-ready template out of the box! For most tasks, **boilpy** consists of a well-defined `Makefile` which can be used to run `make` commands within your project directory.

In order to get started, we recommend you to create a [`.env`](https://12factor.net/config) file within your project directory in order to configure some of the environment variables declared within the `Makefile`. You can override the environment variables defined [here](docs/index.md#environment-variables). To override some of the environment variables, you could also declare them at run-time as follows:

```console
foo@bar:~/foobar$ FOO=BAR BAR=BAZ make [command]
```

#### 1. Configuration

First, create an isolated virtual environment for your package using `virtualenv`:

```console
foo@bar:~/foobar$ make env
→ [20:37:10] Creating a Virtual Environment .venv with Python - /usr/bin/python
```

#### 2. Installation

Simply install your package as follows:

```console
foo@bar:~/foobar$ make
→ [20:38:23] Cleaning Python Cache
→ [20:38:23] Cleaning Successful
→ [20:38:23] Building Requirements
→ [20:38:23] Installing Requirements
→ [20:38:23] Installing foobar (development)
→ [20:38:23] Installation Successful
```

#### 3. Prototyping

To check if your package works, launch the shell:

```console
foo@bar:~/foobar$ make shell
```

...and then simply import your package as follows:

```python
In [1]: import foobar as fb
In [2]: fb.__name__
Out[2]: 'foobar'
```

### License

This repository has been released under the [MIT License](LICENSE).