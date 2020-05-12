from django.test import TestCase
from django.urls import reverse
from rest_framework import status


class PhotoViewTestCase(TestCase):
    def test_get_photo_list_view(self):
        url = reverse("photos:index")
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
