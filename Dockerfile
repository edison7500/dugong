FROM python:3.7.7
ENV PYTHONUNBUFFERED 1
ADD requirements /tmp/requirements
RUN pip install --upgrade pip
RUN pip install -r /tmp/requirements/prod.txt && rm -rf /tmp/requirements
ADD . /opt/dugong
WORKDIR /opt/dugong

EXPOSE 8000

# CMD  ["/usr/bin/supervisord"]
