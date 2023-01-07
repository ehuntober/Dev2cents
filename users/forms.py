from django import forms

from users.models import Newsletter, Profile


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(NewsletterForm, self).__init__(*args, **kwargs)

        self.fields['email'].widget.attrs.update({'class': 'form-control'})


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ["created", "user"]

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control form-label'})
