from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from apps.tutorials.models import Tutorial
from faker import Faker

f = Faker()


class TutorialAPIViewTestCase(APITestCase):
    def setUp(self):
        self.tearDown()

        self.tutorial = Tutorial()
        self.tutorial.title = f.name()
        self.tutorial.content = f.text()
        self.tutorial.tags = f.word()
        self.tutorial.origin_link = f.url()
        self.tutorial.save()

    def tearDown(self):
        Tutorial.objects.all().delete()

    def test_can_get_a_tutorial_list(self):
        url = reverse("api:tutorials:list")
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_can_get_a_tutorial(self):
        url = reverse("api:tutorials:detail", args=[self.tutorial.slug])
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)

        self.tutorial.status = Tutorial.STATUS.published
        self.tutorial.save()
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
