FROM python:3.7.5
ENV PYTHONUNBUFFERED 1
RUN apt-get -y update && apt-get -y install supervisor
RUN apt-get -y purge x11* subversion
RUN apt-get -y autoremove
ADD requirements /tmp/requirements
RUN pip install --upgrade pip
RUN pip install -r /tmp/requirements/prod.txt && rm -rf /tmp/requirements
RUN mkdir -p /opt/dugong
WORKDIR /opt/dugong
#COPY service/gunicorn /etc/default/gunicorn
#COPY service/supervisor.conf /etc/supervisor/conf.d/dugong.conf

EXPOSE 8000

CMD  ["/usr/bin/supervisord"]
