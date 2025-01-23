from django.shortcuts import render
from django.http import HttpResponse
from .model import predict 
import numpy as np

def prediction(request):
    returned_prediction = None
    if request.method == "POST":
        age = int(request.POST.get("age"))
        sex = request.POST.get("sex")
        chestpaintype = request.POST.get("chestpaintype")
        cholestoral = int(request.POST.get("cholestoral"))
        fastingbs = int(request.POST.get("fastingbs"))
        maxhr = int(request.POST.get("maxhr"))
        exerciseangina = request.POST.get("exerciseangina")
        oldpeak = int(request.POST.get("oldpeak"))
        stslope = request.POST.get("stslope")
        
        if sex == "M":
            sex = 0
        else:
            sex = 1

        if chestpaintype == "ASY":
            chestpaintype = 0
        elif chestpaintype == "ATA":
            chestpaintype = 1
        else:
            chestpaintype = 2

        if exerciseangina == "N":
            exerciseangina = 0
        else:
            exerciseangina = 1

        if stslope == "down":
            stslope = 0
        elif stslope == "flat":
            stslope = 1
        else:
            stslope = 2
        user_data = np.array([[age, sex, chestpaintype, cholestoral, fastingbs, maxhr, exerciseangina, oldpeak, stslope]])
        # sample_data = np.array([[24, 1, 0, 198, 0, 140, 0, 0, 2]])
        returned_prediction = predict(user_data)
    return render(request, "prediction/diagnose.html", {"result": returned_prediction})

