# - - - - - Django Imports - - - - - - - - -
from django.forms import ModelForm

# - - - - - Internal imports - - - - - - - - -
from .models import ContactForm


class ContactForm1(ModelForm):
    """
    Form for Contact model that uses all fields
    """
    class Meta:
        model = ContactForm
        fields = '__all__'