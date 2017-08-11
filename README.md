# 概览
[![Build Status](https://travis-ci.org/edison7500/dugong.svg?branch=master)](https://travis-ci.org/edison7500/dugong)

### 系统环境
* Ubuntu
* Python2.7
* MySQL
* Nginx
* Docker

### Web Framework
* *django-1.8.18* [相关文档](https://docs.djangoproject.com/en/1.8/)

### Docker launcher
~~~~.shell
docker run -d -t -i \
        --name dugong \
        -v /data/www/dugong/:/data/www/dugong/ \
        -v /data/www/static/:/data/www/static/ \
        -v /data/www/whoosh_index/:/data/www/whoosh_index \
        -v /tmp:/tmp \
        -p 127.0.0.1:8000:8000 dugong
~~~~


### 教程
* [利用 Django 建站攻略 （一）安装](http://jiaxin.im/blog/li-yong-django-jian-zhan-gong/)
* [利用 Django 建站攻略 （二）建模](http://jiaxin.im/blog/li-yong-django-jian-zhan-gon-1/)
* [利用 Django 建站攻略 （三）视图](http://jiaxin.im/blog/li-yong-django-jian-zhan-gon-2/)
* [利用 Django 建站攻略 （四）搜索](http://jiaxin.im/blog/li-yong-django-jian-zhan-gon-3/)
