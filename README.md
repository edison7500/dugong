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
        -v /data/www/dugong/:/data/www/dugong/ \
        -v /data/www/static/:/data/www/static/ \
        -p 127.0.0.1:8000:8000 dugong
```

### Django 第三方组建
```
django-admin-bootstrapped==2.5.7
django-appconf==1.0.2
django-compressor==2.1
django-debug-toolbar==1.6
django-formtools==1.0
django-simple-captcha==0.5.3
django-wysiwyg-redactor==0.4.9.1
djdt-flamegraph==0.2.12
django-uuslug==1.1.8
django-tagging==0.4.5
django-meta==1.3.2
```
