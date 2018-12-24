from django.core.urlresolvers import reverse
from django.test import TestCase
from rest_framework import status

from tutorials.models import Tutorial

from faker import Faker

f = Faker()


class TutorialListViewTestCase(TestCase):
    def setUp(self):
        self.tutorial = Tutorial()
        self.tutorial.title = f.name()
        self.tutorial.content = f.text()
        self.tutorial.status = Tutorial.STATUS.published
        self.tutorial.origin_link = f.url()
        self.tutorial.save()

    def test_get_tutorial_list(self):
        res = self.client.get(reverse('tutorials:list'))
        self.assertIs(res.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(res, template_name='tutorials/list.html')

    def test_get_tutorial_detail(self):
        _uri = self.tutorial.get_absolute_url()
        res = self.client.get(_uri)
        self.assertIs(res.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(res, template_name='tutorials/detail.html')