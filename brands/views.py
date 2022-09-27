from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
 # from .models import *
from models.models import Model
from brands.models import Brand
# Create your views here.


def main(request):
    data = {
        'brands': Brand.objects.all()
    }
    return render(request, 'brands.html', context=data)


# def brand_detail(request, brand_id):
#     data = {
#         "model": Model.objects.get(id=brand_id)
#     }
#     return render(request, 'detail.html', context=data)

# Create your views here.
