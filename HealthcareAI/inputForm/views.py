from django.shortcuts import render
from .forms import InputForm

# Create your views here.
def inputForm(request):
    context ={}
    context['form']= InputForm()
    return render(request, "inputForm.html", context)
