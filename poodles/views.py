from .models import Poodle, Document, Image
from django.views.generic import (
    TemplateView,
    CreateView,
    UpdateView,
    ListView,
    DetailView
)
from .forms import CrispyPoodleForm, DocumentForm, ImageForm
from django.urls import reverse_lazy
from django.shortcuts import redirect
from choices.views import get_json
from organizer.views import get_person_json
import json


def get_poodle_json(f_sex):
    q = Poodle.objects.filter(sex=f_sex)
    new_lst = []
    obj = {}
    for c in q:
        txt_val = str(c)
        new_lst.append({'value': c.id, 'text': txt_val})
        obj['data'] = new_lst
        j = json.dumps(new_lst)
    return j


class PoodleIndex(TemplateView):
    template_name = 'poodles/index.html'


class PoodleList(ListView):
    model = Poodle
    context_object_name = 'poodles'
    template_name = 'poodles/all.html'
    paginate_by = 10
    queryset = Poodle.objects.all()

    def get_context_data(self, **kwargs):
        context = super(PoodleList, self).get_context_data(**kwargs)
        context['selects'] = {}
        context['selects']['poodle_sire'] = get_poodle_json('M')
        context['selects']['poodle_dam'] = get_poodle_json('F')

        context['selects']['sex'] = get_json('sex')
        context['selects']['color'] = get_json('color')

        context['selects']['person_owner'] = get_person_json()
        context['selects']['person_breeder'] = get_person_json()

        return context


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


class DocumentNew(CreateView):
    model = Document
    form_class = DocumentForm
    template_name = 'poodles/document.html'

    def get_success_url(self):
        """Return the URL to redirect to after processing a valid form."""
        pood = Poodle.objects.get(slug=self.kwargs['slug'])
        url = pood.get_absolute_url()
        return url

    def get_context_data(self, **kwargs):
        context = super(DocumentNew, self).get_context_data(**kwargs)
        pood = Poodle.objects.get(slug=self.kwargs['slug'])
        context['form'] = self.form_class(initial={'poodle': pood})
        return context

    def form_valid(self, form):
        pood = Poodle.objects.get(slug=self.kwargs['slug'])
        form.instance.poodle = pood
        return super(DocumentNew, self).form_valid(form)


class ImageNew(CreateView):
    model = Image
    form_class = ImageForm
    template_name = 'poodles/image.html'

    def get_success_url(self):
        """Return the URL to redirect to after processing a valid form."""
        pood = Poodle.objects.get(slug=self.kwargs['slug'])
        url = pood.get_absolute_url()
        return url

    def get_context_data(self, **kwargs):
        context = super(ImageNew, self).get_context_data(**kwargs)
        pood = Poodle.objects.get(slug=self.kwargs['slug'])
        context['form'] = self.form_class(initial={'poodle': pood})
        return context

    def form_valid(self, form):
        pood = Poodle.objects.get(slug=self.kwargs['slug'])
        form.instance.poodle = pood
        return super(ImageNew, self).form_valid(form)
