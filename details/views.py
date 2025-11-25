from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render
import requests
from decimal import Decimal

from .models import CityWeather
from .utils import q_search


def index(request):
    return render(request, 'details/base.html')


def city_add(request):
    if request.POST.get('action') == "post":
        city = request.POST.get('city_name')
        api_key = 'f958b436fd61ed1e3dd468d57c2895d9'
        s_request = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        )
        if s_request.status_code == 200:
            s_request = s_request.json()
            country = s_request['sys']['country']
            city = s_request['name']
            temp = round(s_request['main']['temp'] - 273.15)
            wind = Decimal(s_request['wind']['speed']).quantize(Decimal("1.0000"))
            weather = s_request['weather'][0]['description']
            cityweather, created = CityWeather.objects.get_or_create(name=city, country=country, temp=temp, wind=wind,
                                                                     weather=weather)
            response = JsonResponse({'city': city, 'country': country, 'temp': temp, 'wind': wind, 'weather': weather})
            return response
        else:
            return render(request, 'details/base.html')


def city_detail(request, pk):
    city = CityWeather.objects.get(id=pk)
    return render(request, 'details/city_detail.html', {'city': city})


def all_cities(request):
    page = request.GET.get('page', 1)
    query = request.GET.get('q', None)
    if query:
        cities = q_search(query)
    else:
        cities = CityWeather.objects.all()
    paginator = Paginator(cities, 3)
    current_page = paginator.page(int(page))
    return render(request, 'details/cities.html', {'cities': current_page})
