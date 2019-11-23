import json

from django.db.models import Q, Count
from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.http import JsonResponse, HttpResponse
from django.core import serializers

from myapp.models import air_quality_cities, air_quality_index,AQI


# Create your views here.

def index(request):
    pollution_list = air_quality_index.objects.order_by('id')
    aqi_list = AQI.objects.order_by('id')
    #aqi_list = [aqi_list]
    quality_list = {
        'access_records': pollution_list,
        'aqi_list': aqi_list,
        'quality': ["table-primary", "table-secondary", "table-success", "table-danger", "table-warning", "table-info"]
    }
    return render(request, 'myapp/index2.html', context=quality_list)


class SearchResult(ListView):
    model = air_quality_cities
    template_name = 'myapp/searchresult.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = air_quality_cities.objects.filter(
            Q(State__icontains=query) | Q(City__icontains=query)
        )
        return object_list


def search(request):
    template_name = 'myapp/searchresult.html'

    query = request.GET.get('q', '')
    if query:
        # query example
        object_list = air_quality_cities.objects.filter(Q(City__icontains=query) | Q(State__icontains=query))
    else:
        object_list = []
    return render(
        request, template_name, {'object_list': object_list})


class SearchPage(TemplateView):
    template_name = 'myapp/index.html'


class About(TemplateView):
    template_name = 'myapp/about.html'


class chart(TemplateView):
    template_name = 'myapp/chart.html'



