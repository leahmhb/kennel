from .models import Person, Kennel
from .forms import CrispyPersonForm, CrispyKennelForm
from django.views.generic import (
    TemplateView,
    CreateView,
    DetailView,
    UpdateView,
    ListView,
    DeleteView,
    FormView
)

from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy


class PersonList(ListView):
    model = Person
    context_object_name = 'people'
    template_name = 'organizer/person/all.html'
    paginate_by = 10
    queryset = Person.objects.all()


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
