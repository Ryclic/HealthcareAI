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
        # converting necessary values
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
        returned_prediction = predict(user_data)
        # Rendering results for user readability
        percent_false = returned_prediction[1][0][0]
        percent_true = returned_prediction[1][0][1]

        if returned_prediction[0] == True:
            returned_prediction = "You may potentially face heart failure. The system predicts with {}% accuracy that heart failure may occur, and with {}% accuracy that it may not.".format(percent_true, percent_false)
        else:
            returned_prediction = "You do not have predicted heart failure. The system predicts with {}% accuracy that heart failure will not occur, and with {}% accuracy that it will.".format(percent_false, percent_true)

    return render(request, "prediction/diagnose.html", {"result": returned_prediction})



# sample_data = np.array([[24, 1, 0, 198, 0, 140, 0, 0, 2]])
# For testing, let's assume we have a sample patient that is 29, M, ASY chest pain, 190 cholestoral, no fasting blood sugar results, max heartrate of 140, no exerciseangina, and downward ST slope
# The other patient will be 24, F, ASY, 190 cholestoral, no fasting blood sugar results, max heartrate of 140, no exercise angina, and upward ST slope



