from django.conf.urls import url
from app import views

urlpatterns = [

    #login page
    url(r'^$', views.index1, name='index1'),
    # Home page
    url(r'^$', views.index, name='index'),


    # Formulario de cliente
    url(r'^$', views.form_cliente, name='form_cliente'),
    # Modificar cliente
    url(r'^$', views.modificar_cliente, name='modificar_cliente'),


    # Formulario de prestamo
    url(r'^$', views.form_prestamo, name='form_prestamo'),
    # Modificar prestamo
    url(r'^$', views.modificar_prestamo, name='modificar_prestamo'),
    # Calculo de prestamos
    url(r'^$', views.calculo_de_prestamos, name='calculo_de_prestamos'),



    # Formulario de usuario
    url(r'^$', views.form_usuario, name='form_usuario'),


    #Listados
    # Recibos al cobro
    url(r'^$', views.recibos_al_cobro, name='recibos_al_cobro'),
    # Recibos despues del cobro
    url(r'^$', views.recibos_despues_del_cobro, name='recibos_despues_del_cobro'),
    # Estados de cuenta
    url(r'^$', views.estados de cuenta, name='estados_de_cuenta'),
    # Historial de cuenta
    url(r'^$', views.historial_de_cuenta, name='historial_de_cuenta'),
    # Relacion de ingresos
    url(r'^$', views.relacion_de_ingresos, name='relacion_de_ingresos'),
]
