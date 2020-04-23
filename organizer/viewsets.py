from rest_framework.viewsets import ModelViewSet

from .models import Kennel, Person
from .serializers import KennelSerializer, PersonSerializer


class PersonViewSet(ModelViewSet):
    lookup_field = 'slug'
    serializer_class = PersonSerializer
    queryset = Person.objects.all().prefetch_related()


class KennelViewSet(ModelViewSet):
    lookup_field = 'slug'
    serializer_class = KennelSerializer
    queryset = Kennel.objects.all().prefetch_related()
