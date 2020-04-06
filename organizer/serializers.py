from .models import Person, Kennel
from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
)
from django.shortcuts import get_object_or_404
from rest_framework.reverse import reverse


class PersonSerializer(ModelSerializer):
    lookup_field = 'slug'
    url = SerializerMethodField()

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

    def to_representation(self, instance):
        data = super().to_representation(instance)
        print(self.kennel)
        tmp_kennel = KennelSerializer(self, Kennel.objects.get(id=self.kennel))
        tmp_kennel_valid = tmp_kennel.is_valid()
        if tmp_kennel_valid:
            tmp_kennel = tmp_kennel.data

        data['kennel'] = tmp_kennel
        return data


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
