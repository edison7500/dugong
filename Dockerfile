# build static
FROM node:12.22.1-buster-slim as frontend
COPY . /opt/dugong
WORKDIR /opt/dugong/frontend/
RUN npm i
RUN npm run build


FROM python:3.7.10-slim-buster
ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get install -y  gcc libpq-dev
COPY requirements /tmp/requirements
RUN pip install --upgrade pip
RUN pip install -r /tmp/requirements/prod.txt --compile && rm -rf /tmp/requirements
RUN mkdir /opt/dugong
COPY . /opt/dugong
WORKDIR /opt/dugong
RUN touch .env

# copy static files from build
COPY --from=frontend /opt/dugong/static/dist /opt/dugong/static/dist
COPY --from=frontend /opt/dugong/static/webpack-stats.json /opt/dugong/static/webpack-stats.json
#RUN python manage.py collectstatic --no-input -i webpack-stats.json -i admin -i rest_framework--settings=dugong.settings.dev

# cleanup
RUN rm -rf /opt/dugong/frontend/
RUN rm -rf /var/lib/apt/lists/*

EXPOSE 8000
