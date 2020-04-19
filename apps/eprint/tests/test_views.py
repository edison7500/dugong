from django.test import TestCase
from django.urls import reverse
from rest_framework import status


class EprintViewTestCase(TestCase):

    def test_get_a_list_views(self):
        _url = reverse("eprint:index")
        res = self.client.get(_url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(res, "eprint/list.html")
