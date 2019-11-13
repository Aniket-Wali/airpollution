from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import air_quality_cities, air_quality_index


# Create your views here.

def index(request):
    pollution_list = air_quality_index.objects.order_by('id')
    quality = {
        'Good': 'table-primary'
    }
    quality_list = {
        'access_records': pollution_list,
        'quality': ["table-primary","table-secondary","table-success","table-danger","table-warning","table-info"]
    }
    return render(request, 'myapp/index2.html', context=quality_list)
