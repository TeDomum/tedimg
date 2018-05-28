FROM python:3-alpine

RUN apk add --no-cache nginx supervisor

ADD . /app
WORKDIR /app

RUN apk add --no-cache nodejs \
 && npm install \
 && npm run build \
 && rm -rf node_modules \
 && apk del nodejs

RUN apk add --no-cache gcc libjpeg-turbo-dev zlib zlib-dev \
 && pip install -r /app/requirements.txt \
 && apk del gcc libjpeg-turbo-dev zlib-dev

EXPOSE 80

CMD /usr/bin/supervisord -c /config/supervisor.conf
