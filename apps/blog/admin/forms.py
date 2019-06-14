# from django import forms
# # from django.utils.translation import ugettext_lazy as _
# from blog.models import Post
# from markdownx.fields import MarkdownxFormField
# 
# 
# class BlogAdminForm(forms.ModelForm):
#     tags = forms.CharField(
#         widget=forms.TextInput(attrs={'class': 'form-control'}),
#         required=False,
#     )
# 
#     def __init__(self, *args, **kwargs):
#         super(BlogAdminForm, self).__init__(*args, **kwargs)
#         self.fields['tags'].initial = ','.join([row.name for row in self.instance.tags.all()])
# 
#     def save(self, commit=True):
#         _tags = self.cleaned_data.get('tags')
#         _obj = super(BlogAdminForm, self).save(commit)
#         self.instance.tags = _tags
#         return _obj
# 
#     class Meta:
#         model = Post
#         fields = forms.ALL_FIELDS
#         widgets = {
#             'content' : MarkdownxFormField(),
#         }


from ajax_select.fields import AutoCompleteSelectMultipleField
from django.forms import ModelForm

# from apps.books.models import Book
from apps.blog.models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = "__all__"

    tags = AutoCompleteSelectMultipleField('tags', required=False, help_text=None)
