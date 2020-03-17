from .models import Poodle, Person
from rest_framework.serializers import (
    HyperlinkedIdentityField,
    ModelSerializer
)


class PoodleSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        lookup_field="akc",
        view_name="poodles:detail"
    )

    class Meta:
        model = Poodle
        fields = '__all__'


class PersonSerializer(ModelSerializer):
    lookup_field = 'id'

    class Meta:
        model = Person
        fields = '__all__'
