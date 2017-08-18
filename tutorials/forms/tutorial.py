from django import forms
from tutorials.models import Tutorial


class TutorialForm(forms.ModelForm):

    class Meta:
        model = Tutorial
        fields = ['title', 'content', 'status', 'tags']
        widgets = {
            'content': forms.Textarea(attrs={"data-provide":"markdown",
                                             "data-iconlibrary":"fa"})
        }

