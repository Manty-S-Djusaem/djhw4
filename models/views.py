from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import *
# Create your views here.


def one_brand(request, brand_id):
    if Model.objects.count() < brand_id:
        return HttpResponse("error. Страница не найдено")
    context = {
        'models': Model.objects.all(),
        'brand': Brand.objects.get(id=brand_id)
    }
    return render(request, 'car.html', context)





def one_brand_series(request, brand_id, model_id):
    context = {
        'model': Model.objects.get(id=model_id),
        'series': Series.objects.filter(model_id=model_id)
    }
    return render(request, 'detail.html', context)
# # Create your views here.

