from django.test import TestCase
from tutorials.models import Tutorial
from faker import Faker

f = Faker()


class TutorialModelTestCase(TestCase):
    def setUp(self):
        self.tutorial = Tutorial()
        self.tutorial.title = f.name()
        self.tutorial.content = f.text()
        self.tutorial.tags = f.word()
        self.tutorial.origin_link = f.url()

    def test_can_create_a_tutorial(self):
        old_count = Tutorial.objects.count()
        self.tutorial.save()
        new_count = Tutorial.objects.count()
        self.assertIsNot(old_count, new_count)