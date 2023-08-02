FROM python:3.9.17-slim-buster
ENV PYTHONUNBUFFERED 1
RUN apt update && apt install -y gcc opencc
COPY requirements /tmp/requirements
RUN pip install -r /tmp/requirements/prod.txt --compile --no-cache-dir && rm -rf /tmp/requirements
RUN mkdir /opt/dugong
RUN touch /opt/dugong/.env
COPY . /opt/dugong
WORKDIR /opt/dugong

# cleanup
RUN rm -rf /var/lib/apt/lists/*
RUN pip cache purge

RUN useradd -s /sbin/nologin -u 1001 -d /opt/dugong dugong
RUN chown dugong .

USER dugong

EXPOSE 8000
