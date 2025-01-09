from django import forms

# creating a form 
class InputForm(forms.Form):
 

    stSlopeChoices = (("flat", "Flat"), ("up", "Up"), ("down", "Down")
    first_name = forms.CharField(max_length = 200)
    last_name = forms.CharField(max_length = 200)
    chestPain = forms.IntegerField(help_text = "0 for asymptomatic, 1 for atypical angina, 2 for non-anginal pain")
    age = forms.IntegerField()
    cholesterol = forms.IntegerField(help_text = "serum cholesterol level in mm/dl")
    maxHeartRate = forms.IntegerField()
    exerciseInducedAngina = forms.BooleanField()
    stSlope = forms.ChoiceField(choices = stSlopeChoices)
    fastingBP = forms.IntegerField(help_text = "1 if fasting BP is above 120, 0 if otherwise")
    oldPeak = forms.DoubleField(help_text = "ECG oldpeak value")
        
