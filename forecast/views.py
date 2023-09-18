from django.shortcuts import render
from .crawler import model
from django.http import JsonResponse, HttpResponse


def index(request):
    return render(request, "forecast/index.html")


def get_forecast(request):
    try:
        _, forecast = model()
        return JsonResponse({"data": forecast.to_dict()})
    except Exception:
        return HttpResponse(status=500)
