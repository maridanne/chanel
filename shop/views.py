from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from .models import DesignerProduct, Category
from django.contrib.auth.decorators import login_required


def search(request): #RETRIEVE
    query = request.GET.get('query', '')
    designerproducts = DesignerProduct.objects.filter(Q(title__contains=query) | Q(description__icontains=query))
    context = {
        'designerproducts': designerproducts,
        'query': query
    }
    return render(request, 'shop/search.html', context)


def category_detail(request, slug): #READ
    category = Category.objects.get(slug=slug)
    designerproducts = category.designerproducts.all()
    context = {
        'category': category,
        'designerproducts': designerproducts
    }
    return render(request, 'shop/category_detail.html', context)
    

def product_detail(request, category_slug, slug): #READ
    product = DesignerProduct.objects.get(slug=slug)
    return render(request, 'shop/product_detail.html', {'product': product})

