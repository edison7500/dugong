from django.test import TestCase
from django.core.urlresolvers import reverse

import factory
from faker import Faker

from django.contrib.auth.models import User
from blog.models import Post
# Create your tests here.
faker = Faker()


class PostFaker(factory.django.DjangoModelFactory):
    class Meta:
        model = Post
        django_get_or_create = ('title', 'content')
    title                   = faker.name()
    content                 = faker.text()


class PostModelTest(TestCase):

    def setUp(self):
        PostFaker()

    def test_post_default_status(self):
        post    = Post.objects.all().last()
        self.assertEqual(post.status, Post.preview)

    def test_model_can_delete_post(self):
        post = Post.objects.all()
        post.delete()
        self.assertEqual(0, post.count())


class PostTemplateTest(TestCase):

    def setUp(self):
        PostFaker()

    def test_post_list(self):
        response     = self.client.get('/blog/')
        self.assertTemplateUsed(response, 'blog/list.html')

    def test_post_detail(self):
        post        = Post.objects.all().first()
        response    = self.client.get('/blog/{slug}/'.format(slug=post.slug))
        self.assertTemplateUsed(response, 'blog/detail.html')



class PostViewTest(TestCase):

    def setUp(self):
        PostFaker()

    def test_post_template(self):
        response    = self.client.get('/blog/')
        self.assertTemplateUsed(response, 'blog/list.html')

    def test_list_view(self):
        res     = self.client.get('/blog/')
        self.assertEqual(res.status_code, 200)

    def test_post_view(self):
        post        = Post.objects.all().last()
        post.status = Post.publish
        post.save()

        path        = reverse('web_blog_detail', args=[post.slug])
        res         = self.client.get(path)
        self.assertEqual(res.status_code, 200)



