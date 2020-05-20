FROM python:3.7.7-slim-buster
ENV PYTHONUNBUFFERED 1
RUN apt update && apt -y install gcc libpq-dev
COPY requirements /tmp/requirements
RUN pip install --upgrade pip
RUN pip install -r /tmp/requirements/prod.txt && rm -rf /tmp/requirements
COPY . /opt/dugong
WORKDIR /opt/dugong
RUN touch .env

EXPOSE 8000

# CMD  ["/usr/bin/supervisord"]
