from rest_framework import viewsets, generics
from poodles.models import Poodle
from poodles.serializers import PoodleSerializer
from pprint import pprint
from rest_framework.decorators import action


class PoodleViewSet(viewsets.ModelViewSet):
    lookup_field = 'slug'
    serializer_class = PoodleSerializer
    queryset = Poodle.objects.all()
