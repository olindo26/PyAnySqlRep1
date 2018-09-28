from django.shortcuts import render
from django.db.models import Q
from AppPyAnySql.models import Datos
# Create your views here.
def index(request):
    context ={
        'Datos_context': Datos.objects.all()
      }
    return render(request, "Index.html", context)
