from rest_framework import routers
from poodles.viewsets import PoodleViewSet
from organizer.viewsets import PersonViewSet, KennelViewSet
router = routers.DefaultRouter()
router.register(r'poodle', PoodleViewSet, basename='poodle')
router.register(r'person', PersonViewSet, basename='person')
router.register(r'kennel', KennelViewSet, basename='kennel')
