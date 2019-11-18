from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from myapp.models import air_quality_cities, air_quality_index


# Create your views here.

def index(request):
    pollution_list = air_quality_index.objects.order_by('id')
    quality_list = {
        'access_records': pollution_list,
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


class SearchPage(TemplateView):
    template_name = 'myapp/index.html'
