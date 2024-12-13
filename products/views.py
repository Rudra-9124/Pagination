from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator

def product_list(request):
    search_query = request.GET.get('search', '') 
    products = Product.objects.filter(name__icontains=search_query)

    # Pagination setup
    paginator = Paginator(products, 5)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'products/product_list.html', {'page_obj': page_obj, 'search_query': search_query})
