from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import FormView
from store.models import Category, Product
from math import ceil
from django.views.generic import ListView
from django import template


#from django.views import View

# Create your views here.
register = template.Library() 


class HomeView(ListView):
    model = Product
    template_name = 'store/index.html'
    context_object_name = 'products'

    def get_context_data(self):
        category_pk = self.request.GET.get("category")
        categories = Category.objects.all()
        if category_pk:
            products = Product.objects.filter(category= category_pk)
            category_pk = int(category_pk)
        else:
            products = Product.objects.all()
        context = {
            'categories' : categories,
            'products' : products,
            'active_category' : category_pk
            }
        return context

     
@register.simple_tag
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
        prodtemp = Product.objects.filter(category=cat)
        prod = [item for item in prodtemp if searchMatch(query, item)]
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        if len(prod) != 0:
            allprods.append([prod, range(1, nSlides), nSlides])
    
    # context = {
    #     'allprods': allprods, 'msg' : ''
    # }
    # if len(allprods) == 0 or len(query)<4:
    #     context = {'msg': 'Please make sure to enter relevant search query'}
    return render(request, template_name='store/search.html')

def about(request):
    return render(request, template_name='store/about.html')

def contactus(request):
    return render(request, template_name='store/contactus.html')

def enquiry(request):
    return render(request, template_name='store/enquiry.html')


