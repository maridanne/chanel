from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Categories'

class DesignerProduct(models.Model):
    user = models.ForeignKey(User, related_name='designerproducts', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='designerproducts', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to='upload/designerproduct_images', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)
    def __str__(self):
        return self.title
