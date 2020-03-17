from rest_framework import routers
from poodles.viewsets import PersonViewSet, PoodleViewSet

router = routers.DefaultRouter()
router.register(r'poodle', PoodleViewSet, basename='poodle')
router.register(r'person', PersonViewSet, basename='person')
