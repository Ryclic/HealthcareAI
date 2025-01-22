from django.http import HttpResponse


def prediction(request):
    return HttpResponse("this is the prediction")
