from django.forms import ModelForm
from shop.models import DesignerProduct, Category

class DesignerProductForm(ModelForm):
    class Meta:
        model = DesignerProduct
        fields = ['user', 'category', 'title', 'slug', 'description', 'price', 'image',]

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['title', 'slug',]
