from store.forms import CheckoutForm
from django.shortcuts import redirect, render
from store.models import Product


import razorpay
client = razorpay.Client(auth=("rzp_test_1ykZ1WTBVrQF5T", "jiSOOiotBl9uqwpV0fs56gky"))


def create_payment(request, slug):
    template_name = ''
    context = {}
    form = CheckoutForm(request.POST)
    product = Product.objects.get(slug=slug)
    user = None
    if request.user.is_authenticated:
        user = request.user
    else:
        return redirect('login')
    if form.is_valid():
        print("Create Payment")
        email = form.cleaned_data.get('email')
        phone = form.cleaned_data.get('phone')
        template_name = 'store/payment.html'
        #create order here
        order_amount = 50000
        order_currency = 'INR'
        order_receipt = 'order_rcptid_11'
        notes = {
            'email': email,
            'phone' : phone
            }   
        data = {
                'amount' : order_amount, 
                'currency' : order_currency, 
                'receipt' : order_receipt, 
                'notes' : notes}     
        order = client.order.create(data=data)
        context = {
            'user' : user,
            'product' : product,
            'order' : order
        }


    else:
        context = {
            'product' : product,
            'form' : form
        }
        template_name = 'store/checkout.html'
    return render(request, template_name=template_name, context=context)