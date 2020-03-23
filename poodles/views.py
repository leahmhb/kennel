from .models import Poodle
from django.views.generic import (
    TemplateView,
    CreateView,
    DetailView,
    UpdateView,
    ListView,
    DeleteView,
    FormView
)
from .forms import CrispyPoodleForm
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect


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
    queryset = Poodle.objects.all()
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    context_object_name = 'poodle'
    template_name = 'poodles/detail.html'


class PoodleNew(CreateView):
    model = Poodle
    form_class = CrispyPoodleForm
    success_url = reverse_lazy('poodles:poodles')
    template_name = 'poodles/new.html'


class PoodleUpdate(UpdateView):
    model = Poodle
    form_class = CrispyPoodleForm
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    context_object_name = 'poodle'
    template_name = 'poodles/update.html'

    def form_valid(self, form):
        poodle = form.save(commit=False)
        poodle.save()
        return redirect('poodles:detail', slug=poodle.slug)
