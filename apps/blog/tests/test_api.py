from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from apps.blog.models import Post
from .post_facker import PostFaker


class PostAPITestCase(APITestCase):

    def setUp(self) -> None:
        self.post = PostFaker()


    def test_post_list_api(self):
        url = reverse("api:blog:index")
        req = self.client.get(url)
        self.assertEqual(req.status_code, status.HTTP_200_OK)

    def test_post_detail_api(self):
        url = reverse("api:blog:detail", args=[self.post.slug])
        req = self.client.get(url)
        self.assertEqual(req.status_code, status.HTTP_404_NOT_FOUND)

        self.post.status = Post.publish
        self.post.save()
        req = self.client.get(url)
        self.assertEqual(req.status_code, status.HTTP_200_OK)
