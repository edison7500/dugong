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