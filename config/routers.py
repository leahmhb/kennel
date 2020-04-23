from rest_framework import routers
from poodles.viewsets import PoodleViewSet, DocumentViewSet, ImageViewSet
from organizer.viewsets import PersonViewSet, KennelViewSet

app_name = 'config'

router = routers.DefaultRouter()
router.register(r'poodle', PoodleViewSet, basename='poodle')
router.register(r'document', DocumentViewSet, basename='document')
router.register(r'image', ImageViewSet, basename='image')

router.register(r'person', PersonViewSet, basename='person')
router.register(r'kennel', KennelViewSet, basename='kennel')
