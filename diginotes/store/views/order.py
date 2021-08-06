from django.shortcuts import render, redirect
from store.models import UserProduct
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def OrderListView(request):
    user = request.user
    orders = UserProduct.objects.filter(user=user)
    return render (request, template_name='store/orders.html', context={'orders' : orders})


