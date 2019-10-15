from django.test import TestCase
from django.urls import reverse


class SearchViewTestCase(TestCase):

    def test_search_index_view(self):
        _url = reverse("search:index")
        res = self.client.get(_url)
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, "search/index.html")
