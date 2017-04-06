# 概览
**我的博客**

### 系统环境
* Ubuntu
* Python2.7
* MySQL
* Nginx
* Docker

### Web Framework
* *django-1.8.15* [相关文档](https://docs.djangoproject.com/en/1.8/)

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

### Django 第三方组建
```
crcmod==1.7
qiniu==7.1.0
Django==1.8.15
django-appconf==1.0.2
django-compressor==2.1
django-debug-toolbar==1.6
django-qiniu-storage==2.3.0
django-formtools==1.0
django-simple-captcha==0.5.3
#django-wysiwyg-redactor==0.5.0
django-uuslug==1.1.8
django-tagging==0.4.5
django-markdown==0.8.4
djangorestframework==3.5.3
django-filter==1.0.1
django-htmlmin==0.10.0
django-cache-machine==0.9.1
gevent==1.1.2
greenlet==0.4.10
gunicorn==19.6.0
Pillow==4.0.0
requests==2.13.0
six==1.10.0
sqlparse==0.2.1
Unidecode==0.4.19
MySQL-python==1.2.5
diskcache==2.3.0

jieba==0.38
Whoosh==2.7.4
django-haystack==2.6.0

django-silk==1.0.0

Pygments==2.1.3
pygments-markdown-lexer==0.1.0.dev39

```

### 教程
* [利用 Django 建站攻略 （一）安装](http://jiaxin.im/blog/li-yong-django-jian-zhan-gong/)
* [利用 Django 建站攻略 （二）建模](http://jiaxin.im/blog/li-yong-django-jian-zhan-gon-1/)
* [利用 Django 建站攻略 （三）视图](http://jiaxin.im/blog/li-yong-django-jian-zhan-gon-2/)
* [利用 Django 建站攻略 （四）搜索](http://jiaxin.im/blog/li-yong-django-jian-zhan-gon-3/)
