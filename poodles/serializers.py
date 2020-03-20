from rest_framework.serializers import (
    HyperlinkedRelatedField,
    ModelSerializer,
    SerializerMethodField,
)
from poodles.models import Poodle
from rest_framework.reverse import reverse

class PoodleSerializer(ModelSerializer):
    lookup_field = 'slug'
    url = SerializerMethodField()

    class Meta:
        model = Poodle
        fields = '__all__'


    def get_url(self, pood):
        """Return full API URL for serialized POST object"""
        return reverse(
            "poodles:one",
            kwargs=dict(
                slug=pood.slug
            ),
            request=self.context["request"],
        )
