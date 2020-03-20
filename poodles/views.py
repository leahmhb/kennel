from .models import Poodle
from rest_framework.response import Response
from django.views.generic import (
    TemplateView,
    CreateView,
    DetailView,
    UpdateView,
    ListView,
    DeleteView,
    FormView
)
from .forms import PoodleForm


class PoodleIndex(TemplateView):
    template_name = 'poodles/index.html'


class PoodleList(ListView):
    model = Poodle
    context_object_name = 'poodles'
    template_name = 'poodles/all.html'
    paginate_by = 10
    queryset = Poodle.objects.all()


class PoodleDetail(DetailView):
    model = Poodle
    form_class = PoodleForm
    queryset = Poodle.objects.all()
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    context_object_name = 'poodle'
    template_name = 'poodles/one.html'
