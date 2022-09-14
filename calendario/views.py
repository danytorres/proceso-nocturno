import re
from django.shortcuts import render

# Create your views here.
def PrimeraPaguina(request):
    return render(request, 'calendario.html')