from apps.blog.models import Post
from apps.blog.tests.post_facker import PostFaker
from django.test import TestCase
# from taggit.models import Tag


class PostModelTest(TestCase):

    def setUp(self):
        PostFaker()

    def test_post_default_status(self):
        post = Post.objects.all().last()
        self.assertEqual(post.status, Post.preview)

    def test_post_update_status(self):
        post = Post.objects.first()
        post.status = Post.publish
        post.save()
        self.assertIs(post.status, Post.publish)

    def test_model_can_delete_post(self):
        post = Post.objects.all()
        post.delete()
        self.assertEqual(0, post.count())

    def test_model_can_add_tags(self):
        post = Post.objects.first()
        post.tags.add("test1,test2,test3")
        tag_count = post.tags.count()
        self.assertIsNot(tag_count, 0)
        # self.assertIsInstance(post.first_tag, Tag)






