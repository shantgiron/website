from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from Inversiones_peniche.models import Vehiculo
from Inversiones_peniche.forms import VehiculoForm


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
