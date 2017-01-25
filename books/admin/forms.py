from django import forms
from books.models import Book


class BookAdminForm(forms.ModelForm):

    tags        = forms.CharField(
                    widget=forms.TextInput(attrs={'class':'form-control'}),
                    required=False,
                )


    def __init__(self, *args, **kwargs):
        super(BookAdminForm, self).__init__(*args, **kwargs)
        self.fields['tags'].initial = ','.join([ row.name for row in self.instance.tags.all()])

    def save(self, commit=True):
        _tags               = self.cleaned_data.get('tags')
        self.instance.tags  = _tags
        return super(BookAdminForm, self).save(commit)

    class Meta:
        model   = Book
        fields  = forms.ALL_FIELDS
        # labels  = {
        #     'creator': _('author'),
        # }
        # widgets = {
        #     'title': forms.TextInput(attrs={'class':'form-control'}),
        #     'status': forms.Select(attrs={'class':'form-control'}),
        # }



