from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Cliente
from .forms import ClienteForm
from Inversiones_peniche.models import Vehiculo
from Inversiones_peniche.forms import VehiculoForm
from .multiforms import MultiFormsView


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


class Clienteform(MultiFormsView):

    form_classes = {'cliente': ClienteForm, 'vehiculo': VehiculoForm}
    template_name = 'app/cliente_form.html'
    success_url = reverse_lazy('inversiones_peniche:index')


"""
class ClienteCreate(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'app/cliente_form.html'
    success_url = reverse_lazy('inversiones_peniche:index')

    # def get(self, request, *args, **kwargs):
    #     clienteform = QuestionForm(self.request.GET or None)
    #     vehiculo_form = AnswerForm(self.request.GET or None)
    #     context = self.get_context_data(**kwargs)
    #     context['answer_form'] = answer_form
    #     context['question_form'] = question_form
    #     return self.render_to_response(context)
"""
class ClienteUpdate(UpdateView, MultiFormsView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'app/cliente_form.html'
    success_url = reverse_lazy('inversiones_peniche:index')
    context_object_name = 'forms.cliente'


"""
class ClienteDelete(DeleteView):
    model = Cliente
    #success_url = reverse_lazy('cliente-list')


class VehiculoCreate(CreateView):
    model = Vehiculo
    form_class = VehiculoForm
    template_name = 'app/cliente_form.html'
    success_url = reverse_lazy('inversiones_peniche:index')
"""

def registro_vehiculo(request):
    if request.method == 'POST':

        form = VehiculoForm(request.POST)
        if form.is_valid():
            matricula = request.POST.get('matricula', '')
            modelo = request.POST.get('modelo', '')
            color = request.POST.get('color', '')
            condicion = request.POST.get('condicion', '')
            valor_mercado = request.POST.get('valor_mercado', '')
            vehiculo_obj = Vehiculo(matricula=matricula, modelo=modelo, color=color, condicion=condicion,
                                    valor_mercado=valor_mercado)
            vehiculo_obj.save()

            # return HttpResponseRedirect(reverse('inversiones_peniche:'))
    else:
        form = VehiculoForm()


    return render(request, 'inversiones_peniche/form_vehiculo.html', {
        'form': form,
    })

