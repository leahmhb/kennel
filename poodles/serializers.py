from rest_framework.serializers import (
    HyperlinkedRelatedField,
    ModelSerializer,
    SerializerMethodField,
)
from poodles.models import Poodle, Document, Image
from rest_framework.reverse import reverse
from organizer.serializers import PersonSerializer


class PoodleSerializer(ModelSerializer):
    lookup_field = 'slug'
    url = SerializerMethodField()
    person_owners = PersonSerializer(many=True)
    person_breeders = PersonSerializer(many=True)

    class Meta:
        model = Poodle
        fields = '__all__'

    def get_url(self, pood):
        """Return full API URL for serialized POST object"""
        return reverse(
            "poodles:detail",
            kwargs=dict(
                slug=pood.slug
            ),
            request=self.context["request"],
        )


class DocumentSerializer(ModelSerializer):
    lookup_field = 'slug'

    class Meta:
        model = Document
        fields = '__all__'


class ImageSerializer(ModelSerializer):
    lookup_field = 'slug'

    class Meta:
        model = Image
        fields = '__all__'
