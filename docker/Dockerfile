FROM        ubuntu:14.04
MAINTAINER	jiaxin	<jiaxin@guoku.com>
RUN         apt-get clean
RUN         apt-get update --fix-missing && apt-get -y install python2.7 \
                    python2.7-dev python-pip gcc make supervisor \
                    libmysqlclient-dev git libjpeg8-dev libpng12-dev zlib1g-dev
COPY        requirements.txt /tmp/requirements.txt
COPY		gunicorn /etc/default/gunicorn
COPY        supervisord.conf /etc/supervisor/conf.d/supervisord.conf

RUN         pip install -r /tmp/requirements.txt
VOLUME		["/data/www/dugong", "/data/www/static"]
WORKDIR     /data/www/dugong
EXPOSE 		8000
CMD         ["/usr/bin/supervisord"]

