from poodles.models import Document, Image, Poodle
from poodles.serializers import (DocumentSerializer, ImageSerializer,
                                 PoodleSerializer)
from rest_framework.viewsets import ModelViewSet


class PoodleViewSet(ModelViewSet):
    lookup_field = 'slug'
    serializer_class = PoodleSerializer
    queryset = Poodle.objects.all().prefetch_related(
                'person_breeders',
                'person_owners')


class DocumentViewSet(ModelViewSet):
    lookup_field = 'slug'
    serializer_class = DocumentSerializer
    queryset = Document.objects.all()


class ImageViewSet(ModelViewSet):
    lookup_field = 'slug'
    serializer_class = ImageSerializer
    queryset = Image.objects.all()
