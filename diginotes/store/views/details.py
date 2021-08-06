from django .shortcuts import HttpResponse, render
from store.models import Product
from django.views.generic import DetailView

#  def product_detail_view(request, slug):
#      product = Product.objects.get(slug=slug)
#      context = {
#          'product' : product
#      }
#      return render(request, template_name='store/product_detail.html', context=context)
  

# class ProductDetailView(View):
#     def get(self, request, slug):
#         product = Product.objects.get(slug=slug)
#         context = {
#             'product' : product
#         }
#         return render(request, template_name='store/product_detail.html', context=context)


class ProductDetailView(DetailView):
    model=Product
