from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class PostAPITestCase(APITestCase):

    def setUp(self) -> None:
        pass

    def test_post_list_api(self):

        url = reverse("api:blog:index")
        req = self.client.get(url)
        self.assertEqual(req.status_code, status)
