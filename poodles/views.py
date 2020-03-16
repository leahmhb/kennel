from .forms import PoodleForm
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, ListView, DeleteView, FormView
from poodles.forms import PoodleForm, PersonForm
from poodles.models import Person, Poodle
from poodles.serializers import PersonSerializer, PoodleSerializer
from pprint import pprint
from rest_framework import generics
import json
from django.shortcuts import get_object_or_404, render

class PoodleIndexView(TemplateView):
    template_name = 'poodles/index.html'


class PoodleListView(ListView):
    model = Poodle
    context_object_name = 'poodles'
    template_name = 'poodles/list.html'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        dv_serializer = PoodleSerializer(Poodle.objects.all(), many=True)
        dv = json.dumps(dv_serializer.data)
        context['poodles'] = dv
        context['url'] = reverse_lazy('poodles:list')
        return context


class PoodleUpdateView(UpdateView):
    model = Poodle
    form_class = PoodleForm
    pk_url_kwarg = 'id'
    context_object_name = 'form'
    success_url = reverse_lazy('poodles:update')
    template_name = 'poodles/update.html'

    def form_valid(self, form):
        return super().form_valid(form)
