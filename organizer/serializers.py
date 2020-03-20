from .models import Person, Kennel
from rest_framework.serializers import (
    HyperlinkedRelatedField,
    ModelSerializer,
    SerializerMethodField,
)

from rest_framework.reverse import reverse


class PersonSerializer(ModelSerializer):
    lookup_field = 'slug'
    url = SerializerMethodField()

    class Meta:
        model = Person
        fields = '__all__'

    def get_url(self, per):
        """Return full API URL for serialized POST object"""
        return reverse(
            "organizer:one-person",
            kwargs=dict(
                slug=per.slug
            ),
            request=self.context["request"],
        )


class KennelSerializer(ModelSerializer):
    lookup_field = 'slug'
    url = SerializerMethodField()

    class Meta:
        model = Kennel
        fields = '__all__'

    def get_url(self, ken):
        """Return full API URL for serialized POST object"""
        return reverse(
            "organizer:one-kennel",
            kwargs=dict(
                slug=ken.slug
            ),
            request=self.context["request"],
        )
