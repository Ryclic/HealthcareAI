from django.shortcuts import render
from django.http import HttpResponse
from .model import predict 
import numpy as np

def prediction(request):
    result = None
    if request.method == "POST":
        user_age = int(request.POST.get("age"))
        print(type(user_age))
        sample_data = np.array([[24, 1, 0, 198, 0, 140, 0, 0, 2]])
        returned_prediction = predict(sample_data)
        
    return render(request, "prediction/diagnose.html", {"result": "test"})

