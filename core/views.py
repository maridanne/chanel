from django.shortcuts import render, redirect
from shop.models import DesignerProduct, Category
from django.contrib.auth.decorators import login_required
from .forms import DesignerProductForm, CategoryForm
from django.contrib import messages
from django.http import HttpResponseRedirect

@login_required(login_url='/user_login/')
def frontpage(request):
    Products = DesignerProduct.objects.all()
    return render(request, 'core/frontpage.html', {'Products' : Products})

def addproduct(request): #CREATE
    form = DesignerProductForm()

    if request.method == 'POST':
        form = DesignerProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            designerproduct = form.cleaned_data.get('title')
            messages.success(request, designerproduct + ' is successfully saved.')
            return redirect('/addproduct/')

    return render(request, 'core/add_product.html', {'form' : form})

def add(request):
    return render(request, 'core/add.html')

def addcategory(request):
    form = CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            category = form.cleaned_data.get('title')
            messages.success(request, category + 'category is successfully saved.')
            return redirect('/addcategory/')

    return render(request, 'core/addcategory.html', {'form' : form})

def updateproduct(request, pk): #UPDATE
    product = DesignerProduct.objects.get(id=pk)
    form = DesignerProductForm(instance=product)

    if request.method == 'POST':
        form = DesignerProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            designerproduct = form.cleaned_data.get('title')
            messages.success(request, designerproduct + ' is successfully updated.')

    context ={
        'form' : form,
        'product' : product
    }

    return render(request, 'core/update_product.html', context)

def deleteproduct(request, pk): #DELETE
    product = DesignerProduct.objects.get(id=pk)
    product.delete()
    messages.success(request, 'The product recently selected was deleted successfully.')
    return render(request, 'core/deletemsg.html')

def deletecategory(request, pk): #DELETE
    category = Category.objects.get(id=pk)
    category.delete()
    messages.success(request, 'The category recently selected was deleted successfully.')
    return render(request, 'core/deletemsg.html')