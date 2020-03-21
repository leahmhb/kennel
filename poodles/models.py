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
from organizer.models import Person
from django_extensions.db.fields import AutoSlugField

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


# Create your models here.


class Poodle(Model):
    slug = AutoSlugField(null=True, default=None,
                         unique=True, populate_from='name_registered')
    name_call = CharField(verbose_name="Call Name", max_length=50)
    name_registered = CharField(verbose_name="Registered Name", max_length=50)
    person_owners = ManyToManyField(
        'organizer.Person',
        verbose_name="Owner(s)",
        related_name='owners')
    person_breeders = ManyToManyField(
        'organizer.Person',
        verbose_name="Breeder(s)",
        related_name='breeders')
    akc = CharField(verbose_name="AKC#", max_length=50)
    chic = CharField(verbose_name="CHIC#", max_length=50,
                     null=True, blank=True, default='')
    ukc = CharField(verbose_name="UKC#", max_length=50,
                    null=True, blank=True, default='')
    sex = CharField(verbose_name="Sex", max_length=1,
                    choices=SEXES, null=True, blank=True)
    is_altered = BooleanField(verbose_name="Altered?", default=False)
    color = CharField(verbose_name="Color", max_length=2,
                      choices=COLORS, null=True, blank=True, default='U')
    dob = DateField(verbose_name="Date of Birth",
                    null=True, blank=True, default='')
    dod = DateField(verbose_name="Date of Death",
                    null=True, blank=True, default='')
    titles_prefix = CharField(
        verbose_name="Prefix Titles",
        max_length=50,
        null=True, blank=True,
        default='')
    titles_suffix = CharField(
        verbose_name="Suffix Titles",
        max_length=50,
        null=True, blank=True,
        default='')
    poodle_sire = ForeignKey('self',
                             verbose_name="Sire", related_name='sire',
                             on_delete=PROTECT,
                             limit_choices_to={'sex': 'M'},
                             null=True, blank=True)
    poodle_dam = ForeignKey('self',
                            verbose_name="Dam", related_name='dam',
                            on_delete=PROTECT,
                            limit_choices_to={'sex': 'F'},
                            null=True, blank=True)

    def __str__(self):
        return self.name_call

    def get_titled_name(self):
        return '%s %s %s' % (self.titles_prefix, self.name_registered, self.titles_suffix)

    def get_owners(self):
        return self.person_owners.all()

    def get_breeders(self):
        return self.person_breeders.all()

    def get_sire(self):
        return self.poodle_sire

    def get_dam(self):
        return self.poodle_dam

    def get_fields(self):
        return [
            (field.verbose_name, field.value_to_string(self))
            for field in Poodle._meta.fields
        ]

    def get_absolute_url(self):
        return reverse('poodles:one', args=[str(self.slug)])

    class Meta:
        app_label = 'poodles'
        db_table = 'poodle'
        verbose_name_plural = 'Poodles'
