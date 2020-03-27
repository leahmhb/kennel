from .models import Person, Kennel
from .forms import CrispyPersonForm, CrispyKennelForm
from django.views.generic import (
    CreateView,
    DetailView,
    UpdateView,
    ListView,
)

from django.shortcuts import redirect
from django.urls import reverse_lazy
from choices.views import get_json
import json


def get_kennel_json():
    q = Kennel.objects.all()
    new_lst = []
    obj = {}
    for c in q:
        txt_val = c.name + ' Standard Poodles'
        new_lst.append({'value': c.id, 'text': txt_val})
        obj['data'] = new_lst
        j = json.dumps(new_lst)
    return j


def get_person_json():
    q = Person.objects.filter()
    new_lst = []
    obj = {}
    for c in q:
        txt_val = str(c)
        new_lst.append({'value': c.id, 'text': txt_val})
        obj['data'] = new_lst
        j = json.dumps(new_lst)
    return j


class PersonList(ListView):
    model = Person
    context_object_name = 'people'
    template_name = 'organizer/person/all.html'
    paginate_by = 10
    queryset = Person.objects.all()

    def get_context_data(self, **kwargs):
        context = super(PersonList, self).get_context_data(**kwargs)
        context['selects'] = {}
        context['selects']['kennels'] = get_kennel_json()
        context['selects']['states'] = get_json('state')
        context['selects']['countries'] = get_json('country')
        return context


class PersonDetail(DetailView):
    model = Person
    queryset = Person.objects.all()
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    context_object_name = 'person'
    template_name = 'organizer/person/detail.html'


class PersonNew(CreateView):
    model = Person
    form_class = CrispyPersonForm
    success_url = reverse_lazy('organizer:people')
    template_name = 'organizer/person/new.html'


class PersonUpdate(UpdateView):
    model = Person
    form_class = CrispyPersonForm
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    context_object_name = 'person'
    template_name = 'organizer/person/update.html'

    def form_valid(self, form):
        person = form.save(commit=False)
        person.save()
        return redirect('organizer:detail-person', slug=person.slug)


class KennelList(ListView):
    model = Kennel
    context_object_name = 'kennels'
    template_name = 'organizer/kennel/all.html'
    paginate_by = 10
    queryset = Kennel.objects.all()

    def get_context_data(self, **kwargs):
        context = super(KennelList, self).get_context_data(**kwargs)
        context['selects'] = {}
        context['selects']['states'] = get_json('state')
        context['selects']['countries'] = get_json('country')
        print(context)
        return context


class KennelNew(CreateView):
    model = Kennel
    form_class = CrispyKennelForm
    success_url = reverse_lazy('organizer:kennels')
    template_name = 'organizer/kennel/new.html'


class KennelDetail(DetailView):
    model = Kennel
    queryset = Kennel.objects.all()
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    context_object_name = 'kennel'
    template_name = 'organizer/kennel/detail.html'


class KennelUpdate(UpdateView):
    model = Kennel
    form_class = CrispyKennelForm
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    context_object_name = 'kennel'
    template_name = 'organizer/kennel/update.html'

    def form_valid(self, form):
        kennel = form.save(commit=False)
        kennel.save()
        return redirect('organizer:detail-kennel', slug=kennel.slug)
