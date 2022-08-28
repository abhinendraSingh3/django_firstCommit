#i have made this app

from django.http import HttpResponse

def index(request):
    return HttpResponse("HELLO THIS IS INDEX")

def about(request):
    return HttpResponse("<h1>About Jod</h1>")