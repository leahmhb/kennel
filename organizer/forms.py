from django.forms import ModelForm
from .models import Person, Kennel
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Button
from crispy_forms.bootstrap import FormActions


class PersonForm(ModelForm):

    class Meta:
        model = Person
        exclude = ['id']


class CrispyPersonForm(PersonForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'form'
        self.helper.form_id = 'person-form'
        self.helper.html5_required = True
        self.helper.layout = Layout(
            Row(
                Column('first_name', css_class='col-md-3 mb-0'),
                Column('mi', css_class='col-md-3 mb-0'),
                Column('last_name', css_class='col-md-3 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('kennel'),
                css_class='form-row'
            ),
            FormActions(
                Submit('save', 'Save'),
                Button('cancel', 'Cancel')
            )
        )


class KennelForm(ModelForm):

    class Meta:
        model = Kennel
        exclude = ['id']


class CrispyKennelForm(KennelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'form'
        self.helper.form_id = 'kennel-form'
        self.helper.html5_required = True
        self.helper.layout = Layout()
