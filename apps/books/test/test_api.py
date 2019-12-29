import logging
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from faker import Faker
from apps.users.tests.faker_user import AdminUserFactory
from rest_framework.authtoken.models import Token

f = Faker()
logger = logging.getLogger("django")


class BookAPITestCase(APITestCase):
    def setUp(self):
        self.admin = AdminUserFactory()
        Token.objects.create(user=self.admin)

    def test_get_book_list(self):
        uri = reverse("api:books:index")
        res = self.client.get(uri, format="json")
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_create_a_book(self):
        uri = reverse("api:books:index")

        payload = {
            "title": f.name(),
            "author": f.user_name(),
            "bio": f.text(),
            "origin_link": f.url(),
            "download_link": f.url(),
        }
        res = self.client.post(uri, data=payload, format="json")
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_a_book_with_admin(self):
        uri = reverse("api:books:index")

        payload = {
            "title": f.name(),
            "author": f.user_name(),
            "bio": f.text(),
            "origin_link": f.url(),
            "download_link": f.url(),
            "tags": [
                f.word()
            ]
        }

        auth_token = self.admin.auth_token.key
        self.client.credentials(HTTP_AUTHORIZATION="Token " + auth_token)
        res = self.client.post(uri, data=payload, format="json")
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
