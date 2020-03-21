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
from django.shortcuts import redirect

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
    template_name = 'organizer/person/detail.html'

class PersonUpdate(UpdateView):
    model = Person
    fields = '__all__'
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


class KennelDetail(DetailView):
    model = Kennel
    form_class = KennelForm
    queryset = Kennel.objects.all()
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    context_object_name = 'kennel'
    template_name = 'organizer/kennel/detail.html'

class KennelUpdate(UpdateView):
    model = Kennel
    fields = '__all__'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    context_object_name = 'kennel'
    template_name = 'organizer/kennel/update.html'

    def form_valid(self, form):
        kennel = form.save(commit=False)
        kennel.save()
        return redirect('organizer:detail-kennel', slug=kennel.slug)