.PHONY: docs test shell

BASEDIR					= $(shell pwd)
-include ${BASEDIR}/.env

ENVIRONMENT				= development

PROJECT					= {{ cookiecutter.slug }}

PROJDIR					= ${BASEDIR}/${PROJECT}
DOCSDIR					= ${BASEDIR}/docs

PYTHONPATH		 	   ?= $(shell command -v python)
VIRTUALENV			   ?= $(shell command -v virtualenv)

VENVDIR				   ?= ${BASEDIR}/.venv
VENVBIN					= ${VENVDIR}/bin

PYTHON				  	= ${VENVBIN}/python
IPYTHON					= ${VENVBIN}/ipython
PIP					  	= ${VENVBIN}/pip
PYTEST					= ${VENVBIN}/pytest
DETOX				  	= ${VENVBIN}/detox
COVERALLS				= ${VENVBIN}/coveralls
TWINE					= ${VENVBIN}/twine
SPHINXBUILD				= ${VENVBIN}/sphinx-build
IPYTHON					= ${VENVBIN}/ipython

JOBS				   ?= $(shell $(PYTHON) -c "import multiprocessing as mp; print(mp.cpu_count())")

NULL					= /dev/null

define log
	$(eval CLEAR     = \033[0m)
	$(eval BOLD		 = \033[0;1m)
	$(eval INFO	     = \033[0;36m)
	$(eval SUCCESS   = \033[0;32m)

	$(eval BULLET 	 = "→")
	$(eval TIMESTAMP = $(shell date +%H:%M:%S))

	@echo "${BULLET} ${$1}[${TIMESTAMP}]${CLEAR} ${BOLD}$2${CLEAR}"
endef

ifndef VERBOSE
.SILENT:
endif

install: clean
ifneq (${VERBOSE},true)
	$(eval OUT = > /dev/null)
endif

	$(call log,INFO,Building Requirements)
	awk '{print}' $(BASEDIR)/requirements/*.txt > $(BASEDIR)/requirements-dev.txt
	cat $(BASEDIR)/requirements/production.txt  > $(BASEDIR)/requirements.txt
		
	$(call log,INFO,Installing Requirements)
	$(PIP) install -r $(BASEDIR)/requirements-dev.txt $(OUT)

	$(call log,INFO,Installing ${PROJECT} (${ENVIRONMENT}))
ifeq (${ENVIRONMENT},development)
	$(PYTHON) setup.py develop $(OUT)
else
	$(PYTHON) setup.py install $(OUT)
endif

	$(call log,SUCCESS,Installation Successful)

clean:
	clear

	$(call log,INFO,Cleaning Python Cache)
	find $(BASEDIR) | grep -E "__pycache__|\.pyc" | xargs rm -rf

	rm -rf \
		$(BASEDIR)/*.egg-info \
		$(BASEDIR)/.pytest_cache \
		$(BASEDIR)/.tox \
		$(BASEDIR)/.coverage* \
		$(BASEDIR)/htmlcov \
		$(BASEDIR)/dist \
		$(BASEDIR)/build \

	$(call log,SUCCESS,Cleaning Successful)

test: install
	$(call log,INFO,Running Python Tests using $(JOBS) jobs.)
	$(DETOX) -n $(JOBS) --skip-missing-interpreters

coverage:
ifeq (${ENVIRONMENT},development)
	$(eval IARGS := --cov-report html)
endif

	$(PYTEST) -n $(JOBS) --cov $(PROJDIR) $(IARGS) $(ARGS)

ifeq (${ENVIRONMENT},development)
	$(PYTHON) -c "import webbrowser as wb; wb.open('file:///${BASEDIR}/htmlcov/index.html')"
endif

ifeq (${ENVIRONMENT},test)
	$(COVERALLS)
endif

docs: install
ifneq (${VERBOSE},true)
	$(eval OUT = > /dev/null)
endif

	$(call log,INFO,Building Documentation)
	$(SPHINXBUILD) $(DOCSDIR)/source $(DOCSDIR)/build $(OUT)

	$(call log,SUCCESS,Building Documentation Successful)

env:
ifneq (${VERBOSE},true)
	$(eval OUT = > /dev/null)
endif

	$(call log,INFO,Creating a Virtual Environment ${VENVDIR} with Python - ${PYTHONPATH})
	$(VIRTUALENV) $(VENVDIR) -p $(PYTHONPATH) $(OUT)

release: test
	$(PYTHON) setup.py sdist bdist_wheel

ifeq (${ENVIRONMENT},development)
	$(call log,WARN,Ensure your environment is in production mode.)
	$(TWINE) upload --repository-url https://test.pypi.org/legacy/   $(BASEDIR)/dist/* 
else
	$(TWINE) upload --repository-url https://upload.pypi.org/legacy/ $(BASEDIR)/dist/* 
endif

shell:
	$(IPYTHON) \
		--no-banner