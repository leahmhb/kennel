from django.db import models

SEXES = (
    ('M', 'Dog'),
    ('F', 'Bitch')
    )

COLORS = (
    ('MP','Multi/Parti'),
    ('WH','White'),
    ('BL','Black'),
    ('BU','Blue'),
    )

# Create your models here.
class Person(models.Model):
    last_name = models.CharField(verbose_name="Last Name", max_length=50)
    first_name = models.CharField(verbose_name="First Name", max_length=50)
    mi = models.CharField(verbose_name="MI", max_length=50, null=True, blank=True)
    kennel_name = models.CharField(verbose_name="Kennel", max_length=50, null=True, blank=True)
    kennel_prefix = models.CharField(verbose_name="Prefix", max_length=50, null=True, blank=True)
    kennel_suffix = models.CharField(verbose_name="Suffix", max_length=50, null=True, blank=True)

    def __str__(self):
        return '%s, %s %s @ %s' % (self.last_name, self.first_name, self.mi, self.kennel_name)

    class Meta:
        db_table = 'person'
        verbose_name_plural = 'People'

class Poodle(models.Model):
    name_call = models.CharField(verbose_name="Call Name", max_length=50)
    name_registered = models.CharField(verbose_name="Registered Name", max_length=50)
    person_owners = models.ManyToManyField(Person, verbose_name="Owner(s)", related_name='owners')
    person_breeders = models.ManyToManyField(Person, verbose_name="Breeder(s)", related_name='breeders')
    akc = models.CharField(verbose_name="AKC#", max_length=50)
    chic = models.CharField(verbose_name="CHIC#", max_length=50, null=True, blank=True)
    ukc = models.CharField(verbose_name="UKC#", max_length=50, null=True, blank=True)
    sex = models.CharField(max_length=1, choices=SEXES, null=True, blank=True)
    is_altered = models.BooleanField(verbose_name="Altered?", default=False)
    color = models.CharField(verbose_name="Color", max_length=2, choices=COLORS, null=True, blank=True)
    dob = models.DateField(verbose_name="Date of Birth", null=True, blank=True)
    dod = models.DateField(verbose_name="Date of Death", null=True, blank=True)
    titles_prefix = models.CharField(verbose_name="Prefix Titles", max_length=50, null=True, blank=True)
    titles_suffix = models.CharField(verbose_name="Suffix Titles", max_length=50, null=True, blank=True)
    poodle_sire = models.ForeignKey('self', verbose_name="Sire", related_name='sire', on_delete=models.PROTECT, limit_choices_to={'sex': 'M'}, null=True, blank=True)
    poodle_dam = models.ForeignKey('self', verbose_name="Dam", related_name='dam', on_delete=models.PROTECT, limit_choices_to={'sex': 'F'}, null=True, blank=True)

    def __str__(self):
        return '%s %s %s (%s)' % (self.titles_prefix, self.name_registered, self.titles_suffix, self.name_call)

    class Meta:
        db_table = 'poodle'
        verbose_name_plural = 'Poodles'