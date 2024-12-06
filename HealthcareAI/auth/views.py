from django.shortcuts import render, HttpResponse

# Create your views here.
def login(request):
    return render(request, "login.html")

def signuabout(request):
    return render(request, "signup.html")
