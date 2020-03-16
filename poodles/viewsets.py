from rest_framework import viewsets, generics
from poodles.models import Poodle, Person
from poodles.serializers import PoodleSerializer, PersonSerializer
from pprint import pprint
from rest_framework.decorators import action


class PersonViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    serializer_class = PersonSerializer
    queryset = Person.objects.all()

class PoodleViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    serializer_class = PoodleSerializer
    queryset = Poodle.objects.all()