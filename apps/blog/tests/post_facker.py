import factory
from apps.blog.models import Post
from faker import Faker

# Create your tests here.
faker = Faker()


class PostFaker(factory.django.DjangoModelFactory):
    class Meta:
        model = Post
        django_get_or_create = ("title", "content")

    title = faker.name()
    content = faker.text()
    # status = Post.publish
