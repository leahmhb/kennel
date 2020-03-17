from django.db import models
from django.db.models import (
    Model, CharField, DateField, ManyToManyField, ForeignKey, BooleanField, PROTECT)

SEXES = (
    ('M', 'Dog'),
    ('F', 'Bitch')
)

COLORS = (
    ('MP', 'Multi/Parti'),
    ('WH', 'White'),
    ('BL', 'Black'),
    ('BU', 'Blue'),
    ('U', 'Unknown')
)


def XSTR(s): return s or ""

# Create your models here.


class Person(Model):
    last_name = CharField(verbose_name="Last Name", max_length=50)
    first_name = CharField(verbose_name="First Name", max_length=50)
    mi = CharField(verbose_name="MI", max_length=50, null=True, blank=True)
    kennel_name = CharField(verbose_name="Kennel",
                            max_length=50, null=True, blank=True)
    kennel_prefix = CharField(verbose_name="Prefix",
                              max_length=50, null=True, blank=True)
    kennel_suffix = CharField(verbose_name="Suffix",
                              max_length=50, null=True, blank=True)

    def __str__(self):

        return XSTR(self.last_name) + ', ' + XSTR(self.first_name) + ' ' + XSTR(self.mi) + ' @ ' + XSTR(self.kennel_name)

    class Meta:
        app_label='poodles'
        db_table = 'person'
        verbose_name_plural = 'People'


class Poodle(Model):
    name_call = CharField(verbose_name="Call Name", max_length=50)
    name_registered = CharField(verbose_name="Registered Name", max_length=50)
    person_owners = ManyToManyField(
        Person, verbose_name="Owner(s)", related_name='owners')
    person_breeders = ManyToManyField(
        Person, verbose_name="Breeder(s)", related_name='breeders')
    akc = CharField(verbose_name="AKC#", max_length=50)
    chic = CharField(verbose_name="CHIC#", max_length=50,
                     null=True, blank=True)
    ukc = CharField(verbose_name="UKC#", max_length=50, null=True, blank=True)
    sex = CharField(max_length=1, choices=SEXES, null=True, blank=True)
    is_altered = BooleanField(verbose_name="Altered?", default=False)
    color = CharField(verbose_name="Color", max_length=2,
                      choices=COLORS, null=True, blank=True)
    dob = DateField(verbose_name="Date of Birth", null=True, blank=True)
    dod = DateField(verbose_name="Date of Death", null=True, blank=True)
    titles_prefix = CharField(
        verbose_name="Prefix Titles", max_length=50, null=True, blank=True)
    titles_suffix = CharField(
        verbose_name="Suffix Titles", max_length=50, null=True, blank=True)
    poodle_sire = ForeignKey('self', verbose_name="Sire", related_name='sire',
                             on_delete=PROTECT, limit_choices_to={'sex': 'M'}, null=True, blank=True)
    poodle_dam = ForeignKey('self', verbose_name="Dam", related_name='dam',
                            on_delete=PROTECT, limit_choices_to={'sex': 'F'}, null=True, blank=True)

    def __str__(self):
        return XSTR(self.titles_prefix) + ' ' + XSTR(self.name_registered) + ' ' + XSTR(self.titles_suffix) + ' (' + XSTR(self.name_call) + ')'

    class Meta:
        app_label='poodles'
        db_table = 'poodle'
        verbose_name_plural = 'Poodles'
