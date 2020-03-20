from django.forms import ModelForm
from poodles.models import Poodle


class PoodleForm(ModelForm):

    class Meta:
        model = Poodle
        exclude = ['id']

