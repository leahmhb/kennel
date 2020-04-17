from django.db.models import (
    Model,
    CharField,
    DateField,
    ManyToManyField,
    ForeignKey,
    BooleanField,
    DateTimeField,
    TextField,
    FileField,
    ImageField,
    PROTECT)
from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from choices.views import get_tuple


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

    def get_absolute_url(self):
        return reverse('poodles:detail', args=[str(self.slug)])

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

    def get_documents(self):
        return Document.objects.filter(poodle=self.id)

    def get_images(self):
        return Image.objects.filter(poodle=self.id)

    def get_fields(self):
        return [
            (field.verbose_name, field.value_to_string(self))
            for field in Poodle._meta.fields
        ]


class Document(Model):
    poodle = ForeignKey(Poodle, verbose_name="Poodle",
                        related_name='poodles_documents',
                        on_delete=PROTECT)
    title = CharField(max_length=255, blank=True)
    description = TextField(blank=True)
    category = CharField(
        max_length=255, choices=get_tuple('category'), blank=True)
    path = FileField(upload_to='documents/')
    is_viewable = BooleanField(verbose_name="Viewable?", default=True)
    uploaded_at = DateTimeField(auto_now_add=True)


class Image(Model):
    poodle = ForeignKey(Poodle, verbose_name="Poodle",
                        related_name='poodles_images',
                        on_delete=PROTECT)
    title = CharField(max_length=255, blank=True)
    description = TextField(blank=True)
    path = ImageField(upload_to='images/')
    is_viewable = BooleanField(verbose_name="Viewable?", default=True)
    uploaded_at = DateTimeField(auto_now_add=True)
