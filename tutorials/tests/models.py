from django.test import TestCase
from tutorials.models import Tutorial


class TutorialModelTestCase(TestCase):
    def setUp(self):
        self.tutorial = Tutorial()
        self.tutorial.title = u''