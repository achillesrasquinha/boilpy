FROM  python:3.7-alpine

LABEL maintainer=achillesrasquinha@gmail.com

ENV {{ cookiecutter.name.upper().replace(' ', '_') }}_PATH=/usr/local/src/{{ cookiecutter.slug }}

RUN apk add --no-cache \
        bash \
        git \
    && mkdir -p ${{ cookiecutter.name.upper().replace(' ', '_') }}_PATH

COPY . ${{ cookiecutter.name.upper().replace(' ', '_') }}_PATH
COPY ./docker/entrypoint.sh /entrypoint.sh

RUN pip install ${{ cookiecutter.name.upper().replace(' ', '_') }}_PATH

WORKDIR ${{ cookiecutter.name.upper().replace(' ', '_') }}_PATH

ENTRYPOINT ["/entrypoint.sh"]

CMD ["{{ cookiecutter.command }}"]