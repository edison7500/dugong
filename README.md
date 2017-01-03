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

