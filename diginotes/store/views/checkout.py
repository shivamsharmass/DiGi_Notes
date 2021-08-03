from store.forms import CheckoutForm
from django.shortcuts import redirect, render
from store.models import Product


def checkout(request, slug):
    if request.user.is_authenticated:
        user = request.user
    else:
        return redirect('login')
    form = CheckoutForm(initial = {'email' : user.email})
    product = Product.objects.get(slug=slug)
    context = {
        'product' : product,
        'form' : form
    }
    return render(request, template_name='store/checkout.html', context=context)