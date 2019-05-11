# coding=utf-8

import os
import sys

import django
import html2text

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)
os.environ['DJANGO_SETTINGS_MODULE'] = 'dugong.settings.production'
django.setup()

from blog.models import Post

p = Post.objects.all()[1:]

# print p.content

for row in p:
    # print row.content
    md = html2text.html2text(row.content)
    # print (md)
    row.content = md
    row.save()
