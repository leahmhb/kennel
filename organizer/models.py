from django.db.models import (
    Model,
    CharField,
    ForeignKey,
    TextField,
    DateTimeField,
    URLField,
    BooleanField,
    PROTECT)
from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from choices.views import get_tuple
from poodles.models import Poodle


class Kennel(Model):
    slug = AutoSlugField(null=True, default=None,
                         unique=True, populate_from='name')
    name = CharField(verbose_name="Name",
                     max_length=50)
    city = CharField(verbose_name="City", max_length=100,
                     null=True, blank=True, default='')
    state = CharField(verbose_name="State", max_length=2,
                      choices=get_tuple('state'), null=True, blank=True)
    country = CharField(verbose_name="Country", max_length=3,
                        choices=get_tuple('country'), null=True, blank=True,
                        default='USA')
    web_url = URLField(verbose_name="Website", blank=True, default='')
    fb_url = URLField(verbose_name="Facebook", blank=True, default='')
    comments = TextField(blank=True, default='')
    created_at = DateTimeField(verbose_name="Created", auto_now_add=True)
    updated_at = DateTimeField(verbose_name="Updated", auto_now=True)

    class Meta:
        app_label = 'organizer'
        db_table = 'kennel'
        verbose_name_plural = 'Kennels'
        ordering = ['name']

    def __str__(self):

        return self.name

    def get_absolute_url(self):
        return reverse('organizer:detail-kennel', args=[str(self.slug)])

    def get_person(self):
        return Person.objects.filter(kennel=self.id)

    def get_owns(self):
        p = list(Person.objects.filter(
            kennel=self.id).values_list('id', flat=True))
        return Poodle.objects.filter(person_owners__in=p).distinct()

    def get_bred(self):
        p = list(Person.objects.filter(
            kennel=self.id).values_list('id', flat=True))
        return Poodle.objects.filter(person_breeders__in=p).distinct()

    def get_fields(self):
        return [
            (field.verbose_name, field.value_to_string(self))
            for field in Kennel._meta.fields
        ]


class Person(Model):
    slug = AutoSlugField(null=True, default=None, unique=True, populate_from=[
                         'last_name', 'first_name', 'mi'])
    last_name = CharField(verbose_name="Last Name", max_length=50)
    first_name = CharField(verbose_name="First Name", max_length=50)
    mi = CharField(verbose_name="MI", max_length=50,
                   null=False, blank=True, default='')
    kennel = ForeignKey(Kennel, verbose_name="Kennel", related_name='kennel',
                        on_delete=PROTECT, null=True, blank=True)
    akc_bred_with_heart = BooleanField(
        verbose_name="AKC Bred with H.E.A.R.T", default=False)
    akc_breeder_of_merit = BooleanField(
        verbose_name="AKC Breeder of Merit", default=False)
    yr_started = CharField(verbose_name="Started",
                           max_length=4, null=False, blank=True, default='')
    comments = TextField(blank=True, default='')
    created_at = DateTimeField(verbose_name="Created", auto_now_add=True)
    updated_at = DateTimeField(verbose_name="Updated", auto_now=True)

    class Meta:
        app_label = 'organizer'
        db_table = 'person'
        verbose_name_plural = 'People'
        ordering = ['last_name']

    def __str__(self):
        return '%s, %s %s' % (self.last_name, self.first_name, self.mi)

    def get_absolute_url(self):
        return reverse('organizer:detail-person', args=[str(self.slug)])

    def get_full_name(self):
        return '%s, %s %s' % (self.last_name, self.first_name, self.mi)

    def get_owns(self):
        return Poodle.objects.filter(person_owners=self.id)

    def get_bred(self):
        return Poodle.objects.filter(person_breeders=self.id)

    def get_fields(self):
        return [
            (field.verbose_name, field.value_to_string(self))
            for field in Person._meta.fields
        ]
