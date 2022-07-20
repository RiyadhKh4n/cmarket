from django import forms
from django.forms import ModelForm
from .models import ContactForm, Newsletter


class ContactForm1(ModelForm):
    """
    Form for Contact model that uses all fields
    """
    class Meta:
        model = ContactForm
        fields = '__all__'


class NewsletterForm(forms.ModelForm):
    """newsletter form"""
    email = forms.EmailField(label='')

    class Meta:
        """newsletter meta class"""
        model = Newsletter
        fields = ('email',)

    def clean_email(self):
        """check if email given already exists in database"""
        email = self.cleaned_data.get("email")
        subscriber = Newsletter.objects.filter(email__iexact=email)
        if subscriber.exists():
            raise forms.ValidationError("This email already exists")
        return email