from rest_framework.reverse import reverse
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from .models import Kennel, Person


class KennelSerializer(ModelSerializer):
    lookup_field = 'slug'
    url = SerializerMethodField()


    class Meta:
        model = Kennel
        fields = '__all__'

    def get_url(self, ken):
        return reverse(
            "organizer:detail-kennel",
            kwargs=dict(
                slug=ken.slug
            ),
            request=self.context["request"],
        )


class PersonSerializer(ModelSerializer):
    lookup_field = 'slug'
    url = SerializerMethodField()
    kennel = KennelSerializer()

    class Meta:
        model = Person
        fields = '__all__'

    def get_url(self, per):
        return reverse(
            "organizer:detail-person",
            kwargs=dict(
                slug=per.slug
            ),
            request=self.context["request"],
        )
