from django.shortcuts import render, redirect
from time import gmtime, strftime
from django.contrib import messages
from .models import *

def index(request):
    print('INDEX METHOD')
    if 'sumPrice' not in request.session:
        request.session['sumPrice'] = 0
        request.session['sumQty'] = 0
        request.session['charge'] = 0
    
    context = {
        'all_items' : Item.objects.all()
    }
    return render(request, 'amadon_app/index.html', context)

def buy(request, id):
    print('CREATE METHOD')
    Item.objects.get(id=id)
    item = Item.objects.get(id=id).__dict__
    print(item['id'])
    print(request.POST['quantity'])
    print(item['price'])
    request.session['charge'] = int(request.POST['quantity']) * float(item['price'])
    print(request.session['charge'])
    request.session['sumQty'] += int(request.POST['quantity'])
    print(request.session['sumQty'])
    request.session['sumPrice'] += float(request.session['charge'])
    request.session
    print('CREATE WORKS!!!!')
    return redirect('/checkout')

def checkout(request):
    print('CHECKOUT METHOD')
    return render(request, 'amadon_app/checkout.html')