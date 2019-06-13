from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class BookAPITestCase(APITestCase):
    def setUp(self) -> None:
        pass

    def test_book_list_api(self):
        uri = reverse("api:books:index")

        res = self.client.get(uri, format="json")

        self.assertEqual(res.status_code, status.HTTP_200_OK)
