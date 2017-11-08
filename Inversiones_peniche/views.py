from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Cliente, Persona
from .forms import PersonaForm


# Create your views here.
def index(request):
    context = {}
    template = loader.get_template('app/index.html')
    return HttpResponse(template.render(context, request))


def gentella_html(request):
    context = {}
    # The template to be loaded as per gentelella.
    # All resource paths for gentelella end in .html.

    # Pick out the html file name from the url. And load that template.
    load_template = request.path.split('/')[-1]
    template = loader.get_template('app/' + load_template)
    return HttpResponse(template.render(context, request))


class ClienteCreate(CreateView):
    form_class = PersonaForm
    model = Persona
    template_name = 'app/cliente_form.html'
    success_url = '/inv/'


class AuthorUpdate(UpdateView):
    model = Cliente


class AuthorDelete(DeleteView):
    model = Cliente
    #success_url = reverse_lazy('cliente-list')