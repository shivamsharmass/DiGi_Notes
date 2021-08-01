from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import FormView
from store.models import Category, Product
from math import ceil


#from django.views import View

# Create your views here.



def home(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, template_name='store/index.html', context=context)
    
def searchMatch(query, item):
    if query in item.name.lower() or item.category.lower() or item.descreption.lower() or item.slug.lower() or item.price.lower():
        return True
    else:
        return False

def search(request):
    query = request.GET.get('search')
    allprods=[]
    catprods= Product.objects.values('category')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prodtemp = Product.filter(Category=cat)
        prod = [item for item in prodtemp if searchMatch(query, item)]
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        if len(prod) != 0:
            allprods.append([prod, range(1, nSlides), nSlides])
    
    context = {
        'allprods': allprods, 'msg' : ''
    }
    if len(allprods) == 0 or len(query)<4:
        context = {'msg': 'Please make sure to enter relevant search query'}
    return render(request, template_name='store/search.html', context=context)

def about(request):
    return HttpResponse("About Page")

def contactus(request):
    return HttpResponse("Contact us Page")

def enquiry(request):
    return HttpResponse("enquiry Page")