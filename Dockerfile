FROM python:3.7.13-slim-buster
ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get install -y gcc opencc
COPY requirements /tmp/requirements
RUN pip install -r /tmp/requirements/prod.txt --compile && rm -rf /tmp/requirements
RUN mkdir /opt/dugong
COPY . /opt/dugong
WORKDIR /opt/dugong
RUN touch .env

# cleanup
RUN rm -rf /var/lib/apt/lists/*

RUN useradd -s /sbin/nologin -u 1001 -d /opt/dugong dugong
RUN chown dugong .

USER dugong

EXPOSE 8000
