<div align="center">
    <img src=".github/assets/logo.png" height="128"> 
    <h1>
        boilpy
    </h1>
    <h4>The Best Python Package Template in the Universe</h4>
</div>

<p align="center">
	<a href="https://saythanks.io/to/achillesrasquinha">
		<img src="https://img.shields.io/badge/Say%20Thanks-🦉-1EAEDB.svg?style=flat-square">
	</a>
	<a href="https://paypal.me/achillesrasquinha">
		<img src="https://img.shields.io/badge/donate-💵-f44336.svg?style=flat-square">
	</a>
</p>

<div align="justify">
	<b>boilpy</b> is a carefully crafted Python Package Template that eases development, testing and production workflow. It heavily emphasizes on <a href="https://en.wikipedia.org/wiki/Convention_over_configuration" target="_blank">convention over configuration</a> so you can focus on getting straight down to building and distributing your python package.
</div>

### Contents

* [Installation](#installation)
* [Usage](#usage)
* [License](#license)

#### Installation

To install [**boilpy**](https://git.io/boilpy), you must first install [`cookiecutter`](https://github.com/audreyr/cookiecutter) as follows:

```console
foo@bar:~$ pip install cookiecutter
```

You can then use `cookiecutter` to fetch and setup **boilpy** as follows:

```console
foo@bar:~$ cookiecutter https://github.com/achillesrasquinha/boilpy
```

#### Usage

**boilpy** provides you a production-ready template out-of-the-box! To get started, we recommend you to create a [`.env`](https://12factor.net/config) file within your project directory to override environment variables declared within the Makefile. You can override the environment variables defined [here](docs/index.md#environment-variables).

##### Configuration

Go ahead and create an isolated virtual environment for your package.

```console
foo@bar:~$ make env
→ [20:37:10] Creating a Virtual Environment .venv with Python - /usr/bin/python
```

##### Installation

Then, simply install your package as follows:

```console
foo@bar:~$ make
→ [20:38:23] Cleaning Python Cache
→ [20:38:23] Cleaning Successful
→ [20:38:23] Building Requirements
→ [20:38:23] Installing Requirements
→ [20:38:23] Installing foobar (development)
→ [20:38:23] Installation Successful
```

##### Testing

To test your package, launch the shell as follows:

```console
foo@bar:~$ make shell
```

...and then simply import your package as follows:

```python
In [1]: import foobar
"Hello, World"
```

#### License

This repository has been released under the [MIT License](LICENSE).