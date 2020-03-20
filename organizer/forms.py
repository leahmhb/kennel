from django.forms import ModelForm
from .models import Person, Kennel


class PersonForm(ModelForm):

    class Meta:
        model = Person
        exclude = ['id']


class KennelForm(ModelForm):

    class Meta:
        model = Kennel
        exclude = ['id']
