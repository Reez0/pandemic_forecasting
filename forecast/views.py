from django.shortcuts import render
from .crawler import model
from django.http import JsonResponse, HttpResponse


def index(request):
    return render(request, "forecast/index.html")


def get_forecast(request):
    try:
        _, forecast = model()
        dict_with_timestamps = forecast['new_cases'].to_dict()
        dict_with_datetimes = {
            str(key): value for key, value in dict_with_timestamps.items()}
        return JsonResponse({"data": dict_with_datetimes})
    except Exception as e:
        print(e)
        return HttpResponse(status=500)
