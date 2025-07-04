from django.shortcuts import render

# Create your views here.
def panel_view(request):
    """
    Render the panel.html template.
    """
    return render(request, 'panel.html')