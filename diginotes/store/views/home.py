from django.core import paginator
from django.db.models.fields import EmailField
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import FormView
from store.models import Category, ContactUs, Product
from math import ceil
from django.views.generic import ListView
from django import template
from django.core.paginator import Paginator
#from django.views import View
from django.views.decorators.csrf import csrf_protect

# Create your views here.
register = template.Library() 


class HomeView(ListView):
    model = Product
    template_name = 'store/index.html'
    context_object_name = 'products'
    paginate_by = 4


    def get_context_data(self):
        page = self.request.GET.get('page')
        if page is None:
            page = 1
        category_pk = self.request.GET.get("category")
        categories = Category.objects.all()
        if category_pk:
            products = Product.objects.filter(category= category_pk, active= True)
        else:
            products = Product.objects.filter(active=True)
        paginator = Paginator(products , self.paginate_by)
        return {
            'categories' : categories,
            'page_obj' : paginator.page(page),
        }

# def home(request):
#     query = request.GET.get('search')
#     results = []
#     products = Product.objects.all()
#     context = {
#         'products' : products
#     }
#     return render(request, template_name='store/search.html', context=context)



def contactus(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        msg = request.POST['message']
        print(name, email, subject, msg)
        contact = ContactUs(name=name, email=email, subject=subject, message=msg)
        contact.save()
    return render(request, template_name='store/contactus.html')

    

     
@register.simple_tag

def searchMatch(query, item):
    '''return true only if query matches the item'''
    if query in item.description.lower() or item.name.lower() or item.category.lower() or item.slug.lower():
        return True
    else:
        return False

def search(request):
    query = request.GET.get('search')
    allProds = []
    catprods = Product.objects.values('category', 'category_id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prodtemp = Product.objects.filter(category=cat)
        prod=[item for item in prodtemp if searchMatch(query, item)]
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        if len(prod)!= 0:
            allProds.append([prod, range(1, nSlides), nSlides])
    context = {'allProds': allProds}
    return render(request, 'store/search.html', context=context)


def about(request):
    return render(request, template_name='store/about.html')


    

def enquiry(request):
    return render(request, template_name='store/enquiry.html')


