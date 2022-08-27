{% set envvar = cookiecutter.name.upper().replace(" ", "_").replace("-", "_") %}

FROM  python:3.7-alpine

ARG DEVELOPMENT=false

LABEL maintainer=achillesrasquinha@gmail.com

ENV {{ envvar }}_PATH=/{{ cookiecutter.name }}

RUN apk add --no-cache \
        bash \
        git \
    && mkdir -p ${{ envvar }}_PATH && \
    pip install --upgrade pip

COPY . ${{ envvar }}_PATH
COPY ./docker/entrypoint.sh /entrypoint
RUN sed -i 's/\r//' /entrypoint \
	&& chmod +x /entrypoint

WORKDIR ${{ envvar }}_PATH

RUN if [[ "${DEVELOPMENT}" ]]; then \
        pip install -r ./requirements-dev.txt; \
        python setup.py develop; \
    else \
        pip install -r ./requirements.txt; \
        python setup.py install; \
    fi

ENTRYPOINT ["/entrypoint"]

CMD ["{{ cookiecutter.command }}"]