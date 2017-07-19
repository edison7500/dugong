from django.test import TestCase

import factory
from faker import Faker

from books.models import Book, Image

# Create your tests here.


faker = Faker()


class BookFaker(factory.django.DjangoModelFactory):
    class Meta:
        model = Book
        django_get_or_create = ('title', 'desc', 'asin', 'price', 'origin_link')

    title                   = faker.name()
    desc                    = faker.text()
    price                   = faker.random_digit()
    asin                    = faker.random_digit()
    origin_link             = faker.url()


class BookModelTest(TestCase):

    def setUp(self):
        BookFaker()

    def test_book_class(self):
        book    = Book.objects.all().first()
        self.assertIsInstance(book, Book)

    def test_model_can_delete_book(self):
        books = Book.objects.all()
        books.delete()
        self.assertEqual(0, books.count())



