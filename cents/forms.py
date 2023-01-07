from django import forms

from cents.models import Cent


class CentsForm(forms.ModelForm):
    class Meta:
        model = Cent
        fields = ["category", "description"]

    def __init__(self, *args, **kwargs):
        super(CentsForm, self).__init__(*args, **kwargs)

        self.fields['category'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'What\'s on your mind?'})
