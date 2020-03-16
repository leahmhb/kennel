from rest_framework import serializers
from poodles.models import Poodle, Person


class PoodleSerializer(serializers.ModelSerializer):
    lookup_field = 'id'
    class Meta:
        model = Poodle
        fields = '__all__'


class PersonSerializer(serializers.ModelSerializer):
    lookup_field = 'id'

    class Meta:
        model = Person
        fields = '__all__'