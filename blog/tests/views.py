from django.core.urlresolvers import reverse
from django.test import TestCase

from blog.models import Post
from blog.tests.post_facker import PostFaker


class PostTemplateTest(TestCase):
    def setUp(self):
        PostFaker()

    def test_post_list(self):
        response = self.client.get('/blog/')
        self.assertTemplateUsed(response, 'blog/list.html')

    def test_post_detail(self):
        post = Post.objects.all().first()
        response = self.client.get('/blog/{slug}/'.format(slug=post.slug))
        self.assertEqual(response.status_code, 404)
        post.status = Post.publish
        post.save()
        response = self.client.get('/blog/{slug}/'.format(slug=post.slug))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/detail.html')


class PostViewTest(TestCase):
    def setUp(self):
        PostFaker()

    def test_post_template(self):
        response = self.client.get('/blog/')
        self.assertTemplateUsed(response, 'blog/list.html')

    def test_list_view(self):
        res = self.client.get('/blog/')
        self.assertEqual(res.status_code, 200)

    def test_post_view(self):
        post = Post.objects.all().last()
        post.status = Post.publish
        post.save()

        path = reverse('web_blog_detail', args=[post.slug])
        res = self.client.get(path)
        self.assertEqual(res.status_code, 200)
