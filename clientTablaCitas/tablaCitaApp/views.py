from django.shortcuts import render

# Create your views here.
def listarTabla(request):
    """
    Renderiza la página principal de la aplicación.
    """
    return render(request, 'listarCita.html')  # Asegúrate de que la ruta al template sea correcta