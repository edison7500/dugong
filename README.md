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
```
docker run -d -t -i \
        --name dugong \
        -v /data/www/dugong/:/data/www/dugong/ \
        -v /data/www/static/:/data/www/static/ \
        -v /data/www/whoosh_index/:/data/www/whoosh_index \
        -v /tmp:/tmp \
        -p 127.0.0.1:8000:8000 dugong
```

### Django 第三方组建
```
django-suit==0.2.23
django-compressor==2.1
django-debug-toolbar==1.6
django-formtools==1.0
django-simple-captcha==0.5.3
django-wysiwyg-redactor==0.4.9.1
django-uuslug==1.1.8
django-tagging==0.4.5
Whoosh==2.7.4
django-haystack==2.6.0
diskcache==2.3.0
```

### 教程
* [利用 Django 建站攻略 （一）安装](http://jiaxin.im/blog/li-yong-django-jian-zhan-gong/)
* [利用 Django 建站攻略 （二）建模](http://jiaxin.im/blog/li-yong-django-jian-zhan-gon-1/)
* [利用 Django 建站攻略 （三）视图](http://jiaxin.im/blog/li-yong-django-jian-zhan-gon-2/)