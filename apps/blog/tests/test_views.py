import logging
from django.core.urlresolvers import reverse
from django.test import TestCase

from blog.models import Post
from blog.tests.post_facker import PostFaker

logger = logging.getLogger("django")



class PostViewTest(TestCase):
    def setUp(self):
        PostFaker()

    def test_post_template(self):
        response = self.client.get(reverse('blog:list'))
        self.assertTemplateUsed(response, 'blog/list.html')

    def test_list_view(self):
        res = self.client.get(reverse('blog:list'))
        self.assertEqual(res.status_code, 200)

    def test_post_view(self):
        post = Post.objects.all().last()
        post.status = Post.publish
        post.save()

        path = reverse('blog:detail', args=[post.slug])
        res = self.client.get(path)
        self.assertEqual(res.status_code, 200)
