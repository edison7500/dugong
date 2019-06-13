import factory
from django.contrib.auth import get_user_model
from faker import Faker

f = Faker()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = get_user_model()
        django_get_or_create = ("username",)

    username = f.user_name()


class AdminUserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = get_user_model()
        django_get_or_create = ("username", "is_staff")

    username = f.user_name()
    is_staff = True
