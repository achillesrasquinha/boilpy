{% set envvar = cookiecutter.name.upper().replace(" ", "_").replace("-", "_") %}

FROM  python:3.7-alpine

LABEL maintainer=achillesrasquinha@gmail.com

ENV {{ envvar }}_PATH=/usr/local/src/{{ cookiecutter.name }}

RUN apk add --no-cache \
        bash \
        git \
    && mkdir -p ${{ envvar }}_PATH

COPY . ${{ envvar }}_PATH
COPY ./docker/entrypoint.sh /entrypoint
RUN sed -i 's/\r//' /entrypoint \
	&& chmod +x /entrypoint

WORKDIR ${{ envvar }}_PATH

RUN pip install -r ./requirements.txt && \
    python setup.py install

ENTRYPOINT ["/entrypoint"]

CMD ["{{ cookiecutter.command }}"]