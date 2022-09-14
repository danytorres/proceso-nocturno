from django.shortcuts import render
from procesos.models import *

# Create your views here.
def ActualizacionProcesos(request):
    tabla_1 = Tabla_23_0.objects.all()
    tabla_2 = Tabla_0_1.objects.all()
    tabla_3 = Tabla_2_3.objects.all()
    tabla_4 = Tabla_3_4.objects.all()
    tabla_5 = Tabla_4_5.objects.all()
    tabla_6 = Tabla_4_5.objects.all()

    tablas = [[tabla_1, "23-0"],[tabla_2,"0-1"],[tabla_3,"1-2"],[tabla_4,"2-3"],[tabla_5,"3-4"],[tabla_6,"4-5"]]
    return render(request, "procesos.html", {"tablas":tablas})