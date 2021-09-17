{% set envvar = cookiecutter.name.upper().replace(" ", "_").replace("-", "_") %}

FROM  python:3.7-alpine

LABEL maintainer=achillesrasquinha@gmail.com

ENV {{ envvar }}_PATH=/usr/local/src/{{ cookiecutter.name }}

RUN apk add --no-cache \
        bash \
        git \
    && mkdir -p ${{ envvar }}_PATH

COPY . ${{ envvar }}_PATH
COPY ./docker/entrypoint.sh /entrypoint.sh

RUN pip install ${{ envvar }}_PATH

WORKDIR ${{ envvar }}_PATH

ENTRYPOINT ["/entrypoint.sh"]

CMD ["{{ cookiecutter.command }}"]