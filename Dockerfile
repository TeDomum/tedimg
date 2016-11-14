FROM python:3

RUN apt-get update \
 && apt-get install --no-install-recommends -y nginx supervisor \
 && apt-get clean

ADD requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

ADD tedimg /tedimg
ADD docker /config

EXPOSE 80

CMD /usr/bin/supervisord -c /config/supervisor.conf
