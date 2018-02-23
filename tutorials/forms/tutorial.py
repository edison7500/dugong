from django import forms
from tutorials.models import Tutorial
# from .widgets import BSMarkDownWidget


class TutorialForm(forms.ModelForm):

    class Meta:
        model = Tutorial
        fields = ['title', 'content', 'status', 'tags', 'origin_link']
        widgets = {
            'content': forms.Textarea()
        }
        # widgets = {
        #     'content': BSMarkDownWidget()
        # }

