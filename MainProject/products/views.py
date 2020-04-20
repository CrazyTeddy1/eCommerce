from django.http import Http404
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from .models import Product


def ProductListView(request):

    queryset = Product.objects.all()
    context = {


        'object_list': queryset
    }

    return render(request, 'MainApp/product_list_view.html', context)




def ProductDetailtListView(request, pk=None, *args, **kwargs):
    #instance = Product.objects.get(pk=pk)#id
    #instance = get_object_or_404(Product, pk=pk)
    try:
        instance = Products.objects.get(id=pk)

    except Product.DoesNotExist:
        print('Product Unavailable')
        raise Http404("Product Unavailable")

    except:
        print('Verify the product that you searching for')
    context = {


        'object': instance
    }

    return render(request, 'MainApp/productDetail.html', context)
