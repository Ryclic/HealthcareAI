from django.shortcuts import render
from django.contrib.auth.forms import UserCreation

def register_view(request):
    form = UserCreationForm()
    return render(request, "")
