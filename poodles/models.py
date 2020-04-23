from django.db.models import (PROTECT, BooleanField, CharField, DateField,
                              DateTimeField, FileField, ForeignKey, ImageField,
                              ManyToManyField, Model, TextField)
from django.urls import reverse

from choices.views import get_tuple
from django_extensions.db.fields import AutoSlugField


class Poodle(Model):
    slug = AutoSlugField(default=None,
                         unique=True, populate_from='name_registered')
    name_call = CharField(verbose_name="Call Name", max_length=50)
    name_registered = CharField(verbose_name="Registered Name", max_length=50)
    person_owners = ManyToManyField(
        'organizer.Person',
        verbose_name="Owner(s)",
        related_name='poodles_owners', blank=True)
    person_breeders = ManyToManyField(
        'organizer.Person',
        verbose_name="Breeder(s)",
        related_name='poodles_breeders', blank=True)
    akc = CharField(verbose_name="AKC#", max_length=50)
    chic = CharField(verbose_name="CHIC#", max_length=50,
                     blank=True, default='')
    ukc = CharField(verbose_name="UKC#", max_length=50,
                    blank=True, default='')
    addtl = CharField(verbose_name="Additional #",
                      max_length=50, blank=True, default='')
    sex = CharField(verbose_name="Sex", max_length=1,
                    choices=get_tuple('sex'))
    is_altered = BooleanField(verbose_name="Altered?", default=False)
    color = CharField(verbose_name="Color", max_length=2,
                      choices=get_tuple('color'), default='U')
    dob = DateField(verbose_name="Date of Birth",
                    null=True, blank=True, default='')
    dod = DateField(verbose_name="Date of Death",
                    null=True, blank=True, default='')
    titles_prefix = CharField(
        verbose_name="Prefix Titles",
        max_length=50,
        blank=True,
        default='')
    titles_suffix = CharField(
        verbose_name="Suffix Titles",
        max_length=50,
        blank=True,
        default='')
    poodle_sire = ForeignKey('self',
                             verbose_name="Sire", related_name='poodles_sire',
                             on_delete=PROTECT,
                             limit_choices_to={'sex': 'M'},
                             null=True, blank=True)
    poodle_dam = ForeignKey('self',
                            verbose_name="Dam", related_name='poodles_dam',
                            on_delete=PROTECT,
                            limit_choices_to={'sex': 'F'},
                            null=True, blank=True)
    comments = TextField(verbose_name="Comments", blank=True, default='')
    created_at = DateTimeField(verbose_name="Created", auto_now_add=True)
    updated_at = DateTimeField(verbose_name="Updated", auto_now=True)

    class Meta:
        app_label = 'poodles'
        db_table = 'poodle'
        verbose_name_plural = 'Poodles'
        ordering = ['updated_at']

    def __str__(self):
        return '%s %s %s "%s"' % (self.titles_prefix, self.name_registered, self.titles_suffix, self.name_call)

    def url(self):
        return reverse('poodles:detail', args=[str(self.slug)])

    def titled_name(self):
        return '%s %s %s' % (self.titles_prefix, self.name_registered, self.titles_suffix)

    def owners(self):
        return self.person_owners.all()

    def breeders(self):
        return self.person_breeders.all()

    def sire(self):
        return self.poodle_sire

    def dam(self):
        return self.poodle_dam

    def documents(self):
        return Document.objects.filter(poodle=self.id)

    def images(self):
        return Image.objects.filter(poodle=self.id)

    def fields(self):
        return [
            (field.verbose_name, field.value_to_string(self))
            for field in Poodle._meta.fields
        ]


class Document(Model):
    slug = AutoSlugField(null=True, default=None, unique=True, populate_from=[
                         'poodle__name_call', 'title', 'id'])
    poodle = ForeignKey(Poodle, verbose_name="Poodle",
                        related_name='poodles_documents',
                        on_delete=PROTECT)
    title = CharField(max_length=255, blank=True)
    description = TextField(blank=True)
    category = CharField(
        max_length=255, choices=get_tuple('category'), blank=True)
    path = FileField(upload_to='documents/')
    is_viewable = BooleanField(verbose_name="Viewable?", default=True)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('poodles:document', args=[str(self.slug)])


class Image(Model):
    slug = AutoSlugField(null=True, default=None, unique=True, populate_from=[
        'poodle__name_call', 'title', 'id'])
    poodle = ForeignKey(Poodle, verbose_name="Poodle",
                        related_name='poodles_images',
                        on_delete=PROTECT)
    title = CharField(max_length=255, blank=True)
    description = TextField(blank=True)
    path = ImageField(upload_to='images/')
    is_viewable = BooleanField(verbose_name="Viewable?", default=True)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('poodles:image', args=[str(self.slug)])
