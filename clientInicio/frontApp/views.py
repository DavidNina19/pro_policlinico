from django.shortcuts import render

# Create your views here.
def inicio_view(request):
    """
    Render the inicio.html template.
    """
    return render(request, 'inicio.html')