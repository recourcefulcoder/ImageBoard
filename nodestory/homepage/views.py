from django.http import HttpResponse


def index(request):
    return HttpResponse("Here we go again...")
