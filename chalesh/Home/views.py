from django.shortcuts import render
from django.http import HttpResponse

# Create your views here. def arshiya_page(request):
def arshiya_page(request):
    person = {'name':'Arshiya'}
    return render(request, 'Arshiya.html', context=person)

def arshiya_name(request):
    car = {'car_name':'BMW'}
    return render(request, 'Arshiya.html', context=car)
