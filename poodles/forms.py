from django.forms import ModelForm
from poodles.models import Person, Poodle


class PersonForm(ModelForm):

    class Meta:
        model = Person
        exclude = ['id']


class PoodleForm(ModelForm):

    class Meta:
        model = Poodle
        exclude = ['id']

