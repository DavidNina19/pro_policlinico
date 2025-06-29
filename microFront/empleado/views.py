from django.shortcuts import render

# Create your views here.
def horaView(request):
    return render(request, 'getEmpleado.html')