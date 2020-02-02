from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase


class ExChangeRateAPITestCase(APITestCase):

    def setUp(self) -> None:
        pass

    def test_exchange_rate_list_view(self):
        url = reverse("api:exchangerate:index")
        req = self.client.get(url)
        self.assertEqual(req.status_code, status.HTTP_200_OK)
