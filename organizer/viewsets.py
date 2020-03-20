from rest_framework import viewsets, generics
from .models import Person, Kennel
from .serializers import PersonSerializer, KennelSerializer
from pprint import pprint
from rest_framework.decorators import action


class PersonViewSet(viewsets.ModelViewSet):
    lookup_field = 'slug'
    serializer_class = PersonSerializer
    queryset = Person.objects.all()


class KennelViewSet(viewsets.ModelViewSet):
    lookup_field = 'slug'
    serializer_class = KennelSerializer
    queryset = Kennel.objects.all()
