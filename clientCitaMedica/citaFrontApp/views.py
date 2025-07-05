from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Decorador login_required: Redirige al LOGIN_URL si el usuario no está autenticado
@login_required
def cita_medica_view(request):
    return render(request, 'cita_medica.html', {})