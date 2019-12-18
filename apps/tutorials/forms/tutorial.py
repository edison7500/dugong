from django import forms
from apps.tutorials.models import Tutorial
# from editormd.fields import EditorMdFormField


class TutorialForm(forms.ModelForm):

    class Meta:
        model = Tutorial
        fields = ['title', 'content', 'status', 'origin_link']
        # widgets = {
        #     'content': EditorMdFormField(),
        # }
        # widgets = {
        #     'content': BSMarkDownWidget()
        # }

