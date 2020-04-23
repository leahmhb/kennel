from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DetailView, ListView,
                                  TemplateView, UpdateView)

from .forms import CrispyPoodleForm, DocumentForm, ImageForm
from .models import Document, Image, Poodle


class PoodleIndex(TemplateView):
    template_name = 'poodles/index.html'


class PoodleList(ListView):
    model = Poodle
    context_object_name = 'poodles'
    template_name = 'poodles/poodle/all.html'
    paginate_by = 10
    queryset = Poodle.objects.all()

    def get_context_data(self, **kwargs):
        context = super(PoodleList, self).get_context_data(**kwargs)
        return context


class PoodleDetail(DetailView):
    model = Poodle
    queryset = Poodle.objects.all()
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    context_object_name = 'poodle'
    template_name = 'poodles/poodle/detail.html'

    def get_context_data(self, **kwargs):
        context = super(PoodleDetail, self).get_context_data(**kwargs)
        return context


class PoodleNew(CreateView):
    model = Poodle
    form_class = CrispyPoodleForm
    success_url = reverse_lazy('poodles:poodles')
    template_name = 'poodles/poodle/form.html'

    def get_context_data(self, **kwargs):
        context = super(PoodleNew, self).get_context_data(**kwargs)
        context['action'] = 'new'
        return context


class PoodleUpdate(UpdateView):
    model = Poodle
    form_class = CrispyPoodleForm
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    context_object_name = 'poodle'
    template_name = 'poodles/poodle/form.html'

    def form_valid(self, form):
        poodle = form.save()
        return redirect('poodles:detail', slug=poodle.slug)

    def get_context_data(self, **kwargs):
        context = super(PoodleNew, self).get_context_data(**kwargs)
        context['action'] = 'update'
        return context


class DocumentNew(CreateView):
    model = Document
    form_class = DocumentForm
    template_name = 'poodles/document/form.html'

    def get_success_url(self):
        """Return the URL to redirect to after processing a valid form."""
        pood = Poodle.objects.get(slug=self.kwargs['slug'])
        url = pood.get_absolute_url()
        return url

    def get_context_data(self, **kwargs):
        context = super(DocumentNew, self).get_context_data(**kwargs)
        pood = Poodle.objects.get(slug=self.kwargs['slug'])
        context['form'] = self.form_class(initial={'poodle': pood})
        context['action'] = 'new'
        return context

    def form_valid(self, form):
        pood = Poodle.objects.get(slug=self.kwargs['slug'])
        form.instance.poodle = pood
        return super(DocumentNew, self).form_valid(form)


class DocumentUpdate(UpdateView):
    model = Document
    form_class = DocumentForm
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    context_object_name = 'document'
    template_name = 'poodles/document/update.html'

    def get_success_url(self):
        """Return the URL to redirect to after processing a valid form."""
        pood = Poodle.objects.get(slug=self.kwargs['slug'])
        url = pood.get_absolute_url()
        return url

    def get_context_data(self, **kwargs):
        context = super(DocumentNew, self).get_context_data(**kwargs)
        pood = Poodle.objects.get(slug=self.kwargs['slug'])
        context['form'] = self.form_class(initial={'poodle': pood})
        context['action'] = 'update'
        return context

    def form_valid(self, form):
        pood = Poodle.objects.get(slug=self.kwargs['slug'])
        form.instance.poodle = pood
        return super(DocumentUpdate, self).form_valid(form)


class ImageNew(CreateView):
    model = Image
    form_class = ImageForm
    template_name = 'poodles/image/form.html'

    def get_success_url(self):
        """Return the URL to redirect to after processing a valid form."""
        pood = Poodle.objects.get(slug=self.kwargs['slug'])
        url = pood.get_absolute_url()
        return url

    def get_context_data(self, **kwargs):
        context = super(ImageNew, self).get_context_data(**kwargs)
        pood = Poodle.objects.get(slug=self.kwargs['slug'])
        context['form'] = self.form_class(initial={'poodle': pood})
        context['action'] = 'new'
        return context

    def form_valid(self, form):
        form.instance.poodle = Poodle.objects.get(slug=self.kwargs['slug'])
        return super(ImageNew, self).form_valid(form)


class ImageUpdate(CreateView):
    model = Image
    form_class = ImageForm
    template_name = 'poodles/image/form.html'

    def get_success_url(self):
        """Return the URL to redirect to after processing a valid form."""
        pood = Poodle.objects.get(slug=self.kwargs['slug'])
        url = pood.get_absolute_url()
        return url

    def get_context_data(self, **kwargs):
        context = super(ImageUpdate, self).get_context_data(**kwargs)
        pood = Poodle.objects.get(slug=self.kwargs['slug'])
        context['form'] = self.form_class(initial={'poodle': pood})
        context['action'] = 'new'
        return context

    def form_valid(self, form):
        form.instance.poodle = Poodle.objects.get(slug=self.kwargs['slug'])
        return super(ImageUpdate, self).form_valid(form)
