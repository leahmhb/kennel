from django.db import models
from django.db.models import (
    Model,
    CharField,
    DateField,
    ManyToManyField,
    ForeignKey,
    BooleanField,
    PROTECT)
from django.urls import reverse
from django_extensions.db.fields import AutoSlugField


def XSTR(s): return s or ""
# Create your models here.


class Kennel(Model):
    slug = AutoSlugField(null=True, default=None,
                         unique=True, populate_from='name')
    name = CharField(verbose_name="Name",
                     max_length=50)
    city = CharField(verbose_name="City", max_length=100,
                     null=True, blank=True)
    state = CharField(verbose_name="State", max_length=2,
                      null=True, blank=True)
    country = CharField(verbose_name="Country", max_length=3,
                        null=True, blank=True, default='USA')

    def __str__(self):

        return self.name

    def get_absolute_url(self):
        return reverse('organizer:detail-kennel', args=[str(self.slug)])

    def get_fields(self):
        return [
            (field.verbose_name, field.value_to_string(self))
            for field in Kennel._meta.fields
        ]

    class Meta:
        app_label = 'organizer'
        db_table = 'kennel'
        verbose_name_plural = 'Kennels'


class Person(Model):
    slug = AutoSlugField(null=True, default=None, unique=True, populate_from=[
                         'last_name', 'first_name', 'mi'])
    last_name = CharField(verbose_name="Last Name", max_length=50)
    first_name = CharField(verbose_name="First Name", max_length=50)
    mi = CharField(verbose_name="MI", max_length=50, null=True, blank=True)
    kennel = ForeignKey(Kennel, verbose_name="Kennel", related_name='kennel',
                        on_delete=PROTECT, null=True, blank=True)

    def __str__(self):
        return '%s, %s %s' % (self.last_name, self.first_name, self.mi)

    def get_full_name(self):
        return '%s, %s %s' % (self.last_name, self.first_name, self.mi)

    def get_kennel(self):
        return self.kennel

    def get_absolute_url(self):
        return reverse('organizer:detail-person', args=[str(self.slug)])

    def get_fields(self):
        return [
            (field.verbose_name, field.value_to_string(self))
            for field in Person._meta.fields
        ]

    class Meta:
        app_label = 'organizer'
        db_table = 'person'
        verbose_name_plural = 'People'
