from django.shortcuts import render

# Create your views here.
def obtener_login(request):
    return render(request, 'web_app/login.html')