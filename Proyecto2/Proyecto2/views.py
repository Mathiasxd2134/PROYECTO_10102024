from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Bienvenidos Alumnos a nuestra primera sesion de Django")
