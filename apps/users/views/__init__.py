from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin


class UserProfileView(LoginRequiredMixin, generic.DetailView):
    template_name = "account/profile.html"
    model = User
    queryset = User.objects.filter(is_active=True)
