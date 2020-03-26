from django.db.models import (
    Model,
    CharField,
    DateTimeField,
    BooleanField)
from django_extensions.db.fields import AutoSlugField


class Choice(Model):
    field = CharField(verbose_name="Model Field", max_length=50)
    code = CharField(verbose_name="Code", max_length=2)
    text = CharField(verbose_name="Text", max_length=50)
    is_active = BooleanField(verbose_name="Active?", default=True)
    created_at = DateTimeField(verbose_name="Created", auto_now_add=True)

    class Meta:
        app_label = 'choices'
        db_table = 'choice'
        verbose_name_plural = 'Choices'
        ordering = ['field', 'code', 'text']

    def __str__(self):

        return '%s: (%s) %s' % (self.field, self.code, self.text)
