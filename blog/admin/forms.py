from django import forms
from django.utils.translation import ugettext_lazy as _
from blog.models import Post

class BlogAdminForm(forms.ModelForm):

    class Meta:
        model   = Post
        fields  = forms.ALL_FIELDS
        # labels  = {
        #     'creator': _('author'),
        # }
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'status': forms.Select(attrs={'class':'form-control'}),
        }



