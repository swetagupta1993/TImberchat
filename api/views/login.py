from django.http import HttpResponse

def login(request):
    return HttpResponse("Login page from API")