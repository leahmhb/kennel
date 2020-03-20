from .models import Person, Kennel
from django.views.generic import (
    TemplateView,
    CreateView,
    DetailView,
    UpdateView,
    ListView,
    DeleteView,
    FormView
)
from .forms import PersonForm, KennelForm


class PersonList(ListView):
    model = Person
    context_object_name = 'people'
    template_name = 'organizer/person/all.html'
    paginate_by = 10
    queryset = Person.objects.all()


class PersonDetail(DetailView):
    model = Person
    form_class = PersonForm
    queryset = Person.objects.all()
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    context_object_name = 'person'
    template_name = 'organizer/person/one.html'


class KennelList(ListView):
    model = Kennel
    context_object_name = 'kennels'
    template_name = 'organizer/kennel/all.html'
    paginate_by = 10
    queryset = Kennel.objects.all()


class KennelDetail(DetailView):
    model = Kennel
    form_class = KennelForm
    queryset = Kennel.objects.all()
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    context_object_name = 'kennel'
    template_name = 'organizer/kennel/one.html'
