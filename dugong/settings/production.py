from settings import *

DEBUG = False


ALLOWED_HOSTS = ['jiaxin.im', 'www.jiaxin.im', 'api.jiaxin.im']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dugong',
        'USER': 'dugong',
        'PASSWORD': 'dugong123',
        'HOST': '/tmp/mysql.sock',
        'PORT': 3306,
        'OPTIONS': {
            'charset': 'utf8',
            'init_command': 'SET storage_engine=INNODB',
        }
    }
}

STATIC_URL              = '//static.jiaxin.im/static/'
STATIC_ROOT             = '/data/www/static/'
# COMPRESS_URL            =   '/static/'



COMPRESS_ENABLED        = True

INSTALLED_APPS  += (
    'gunicorn',
)

'''
    storage configure
'''
DEFAULT_FILE_STORAGE        = 'storages.backends.qiniustorage.QiNiuStorage'
REDACTOR_FILE_STORAGE       = 'storages.backends.qiniustorage.QiNiuStorage'

FILE_UPLOAD_MAX_MEMORY_SIZE = 5242880
IMAGE_HOST                  = '//imgjiaxin.u.qiniudn.com/'
# IMAGE_HOST = 'https://dn-jiaxin.qbox.me/'

QINIU_ACCESS_KEY            = "xD6MU4_jZANfAqu9auFQm4qkSIx_ln2hIefKIFAU"
QINIU_SECRET_KEY            = "NkTHwgTFQHFaujEB3Fo-ZC2jgf6LkjkWT0iWbwWP"
QINIU_BUCKET                = "imgjiaxin"
