from django.shortcuts import render
from .models import Bmi

def home(request):
    context={}
    if request.method == "POST":
        weight_metric = request.POST.get("weight-metric")
        weight_imperial = request.POST.get("weight-imperial")
        if weight_metric:
            weight = float(request.POST.get("weight-metric"))
            height = float(request.POST.get("height-metric"))
        elif weight_imperial:
            weight = float(request.POST.get("weight-imperial")) / 2.205
            height = (float(request.POST.get("feet")) * 30.48 + float(request.POST.get("inches")) * 2.54) / 100
        bmi = (weight / (height ** 2))
        save = request.POST.get("save")
        if save == "on":
            Bmi.objects.create(user=request.user, weight=weight, height=height, bmi=round(bmi))
        if bmi < 16:
            state = "Severe Thinness"
        elif bmi > 16 and bmi < 17:
            state = "Moderate Thinness"
        elif bmi > 17 and bmi < 18:
            state = "Mild Thinness"
        elif bmi > 18 and bmi < 25:
            state = "Normal"
        elif bmi > 25 and bmi < 30:
            state = "Overweight"
        elif bmi > 30 and bmi < 35:
            state = "Obese Class I"
        elif bmi > 35 and bmi < 40:
            state = "Obese Class II"
        elif bmi > 40:
            state = "Obese Class III"
        context["bmi"] = round(bmi)
        context["state"] = state
    return render(request, "bmi/index.html", context)
