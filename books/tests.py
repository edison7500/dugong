from django.test import TestCase

import factory
from faker import Faker

from books.models import Book

# Create your tests here.


faker = Faker()



class BookFaker(factory.django.DjangoModelFactory):
    class Meta:
        model = Book
        django_get_or_create = ('title', 'desc', 'price', 'source', 'buy_link')

    title                   = faker.name()
    desc                    = faker.text()
    price                   = faker.random_digit()
    source                  = faker.domain_name()
    buy_link                = faker.url()


class BookModelTest(TestCase):

    def setUp(self):
        BookFaker()

    def test_book_class(self):
        book    = Book.objects.all().first()
        self.assertIsInstance(book, Book)
