import factory
from faker import Faker
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from apps.books.models import Book

f = Faker()


class BookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Book

    title = f.name()


class BookAPITestCase(APITestCase):

    def setUp(self) -> None:
        BookFactory()

    def test_get_books(self):
        _uri = reverse("api:book:list")
        res = self.client.get(_uri)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    # def test_create_book(self):
    #     pass
