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
                Column('first_name', css_class='col-md-5 mb-0'),
                Column('mi', css_class='col-md-2 mb-0'),
                Column('last_name', css_class='col-md-5 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('kennel'),
                css_class='form-row'
            ),
            Row(
                Column('yr_started', css_class='col-md-4 mb-0'),
                Column('akc_breeder_of_merit', css_class='col-md-4 mb-0'),
                Column('akc_bred_with_heart', css_class='col-md-4 mb-0'),
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
        self.helper.layout = Layout(
            Row(
                Column('name'),
                css_class='form-row'
            ),
            Row(
                Column('city', css_class='col-md-4 mb-0'),
                Column('state', css_class='col-md-4 mb-0'),
                Column('country', css_class='col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('web_url', css_class='col-md-6 mb-0'),
                Column('fb_url', css_class='col-md-6 mb-0'),

                css_class='form-row'
            ),
            Row(
                Column('comments'),
                css_class='form-row'
            ),
            FormActions(
                Submit('save', 'Save'),
                Button('cancel', 'Cancel')
            ))
