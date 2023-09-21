FROM python:3.6-slim-jessie

RUN mkdir /code

WORKDIR /code

ADD requirements.txt /code

RUN apt-get update && \
    apt-get install --force-yes --assume-yes gcc make axel python3-dev libssl-dev mysql-client libmysqld-dev libffi-dev \
    fontconfig xfonts-75dpi xfonts-base libpng12-0 nano vim telnet libxrender1 libfontconfig1 \
    wget libx11-dev libjpeg62 libxtst6

RUN pip install --upgrade pip
RUN pip install -r requirements.txt --use-feature=2020-resolver

ADD . /code/

EXPOSE 8002

CMD gunicorn --workers=1 --threads=2 --worker-class=gthread --access-logfile=- --timeout=300 \
-e SENTRY=$SENTRY \
-e API_PATH=$API_PATH \
-e SECRET_KEY=$SECRET_KEY \
-e ACCESS_TOKEN_EXPIRE_SECONDS=$ACCESS_TOKEN_EXPIRE_SECONDS \
-e DATABASE_NAME=$DATABASE_NAME \
-e DATABASE_USER=$DATABASE_USER \
-e DATABASE_PASSWORD=$DATABASE_PASSWORD \
-e DATABASE_HOST=$DATABASE_HOST \
-e DATABASE_PORT=$DATABASE_PORT \
--bind 0.0.0.0:8002 estoque_geral.wsgi