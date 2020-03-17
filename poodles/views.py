from django.views.generic import TemplateView
from .models import Poodle
from .serializers import PoodleSerializer
from pprint import pprint
from django.shortcuts import (
    get_list_or_404,
    get_object_or_404
)


from rest_framework.response import Response
from rest_framework.views import APIView


class PoodleIndex(TemplateView):
    template_name = 'poodles/index.html'


class PoodleDetail(APIView):
    template_name = 'poodles/detail.html'

    def get(self, request, akc):
        pood = get_object_or_404(Poodle, akc=akc)
        s_pood = PoodleSerializer(pood, context={"request": request})
        return Response(s_pood.data)


class PoodleList(APIView):
    model = Poodle
    context_object_name = 'poodles'
    template_name = 'poodles/list.html'
    paginate_by = 20

    def get(self, request):
        poods = get_list_or_404(Poodle)
        s_poods = PoodleSerializer(
            poods, many=True, context={"request": request})
        return Response(s_poods.data)
