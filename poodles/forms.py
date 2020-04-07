from django.forms import ModelForm
from poodles.models import Poodle, Document, Image
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit, Row, Column, Button
from crispy_forms.bootstrap import FormActions


class DocumentForm(ModelForm):
    class Meta:
        model = Document
        exclude = ['id']


class ImageForm(ModelForm):
    class Meta:
        model = Image
        exclude = ['id']


class PoodleForm(ModelForm):
    class Meta:
        model = Poodle
        exclude = ['id']


class CrispyPoodleForm(PoodleForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_class = 'form'
        self.helper.form_id = 'poodle-form'
        self.helper.html5_required = True
        self.helper.layout = Layout(
            Row(
                Column('name_call', css_class='col-md-3 mb-0'),
                Column(Field('color'), css_class='col-md-3 mb-0'),
                Column(Field('sex'), css_class='col-md-3 mb-0'),
                Column(Field('is_altered', wrapper_class="form-check"),
                       css_class='col-md-3 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('titles_prefix', css_class='form-group col-md-4 mb-0'),
                Column('name_registered', css_class='form-group col-md-4 mb-0'),
                Column('titles_suffix', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('person_owners', css_class='form-group col-md-6 mb-0'),
                Column('person_breeders', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('dob', css_class='form-group col-md-6 mb-0'),
                Column('dod', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('akc', css_class='form-group col-md-3 mb-0'),
                Column('chic', css_class='form-group col-md-3 mb-0'),
                Column('addtl', css_class='form-group col-md-3 mb-0'),
                Column('ukc', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('poodle_sire', css_class='form-group col-md-6 mb-0'),
                Column('poodle_dam', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('comments', css_class='form-group col-md-12 mb-0'),
                css_class='form-row'
            ),
            FormActions(
                Submit('save', 'Save'),
                Button('cancel', 'Cancel')
            )
        )
