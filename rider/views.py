from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html',{'products': products})
#    return HttpResponse("yo. My mission for this year was to get a source of income; job or something that pays me sensible money. This would facilitate me to get a girl friend so as to quench my sexual desires. I seem to have got a girl friend in the names of None of your business, I had, midyear that is set my goal to getting a drawing tablet, it is here with me. What really remains in the mission is the sensible source of income.")