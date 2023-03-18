from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from core.views import frontpage, addproduct, updateproduct, deleteproduct, add, addcategory, deletecategory
admin.site.site_header = "CHANEL"
admin.site.site_title = "CHANEL"
# admin.site.index_title = "CHANEL"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('userprofile.urls')),
    path('add/', add, name='add'),
    path('addproduct/', addproduct, name='addproduct'),
    path('addcategory/', addcategory, name='addcategory'),
    path('updateproduct/<pk>/', updateproduct, name='updateproduct'),
    path('deleteproduct/<pk>/', deleteproduct, name='deleteproduct'),
    path('deletecategory/<pk>/', deletecategory, name='deletecategory'),
    path('', include('shop.urls')),
    path('', frontpage, name='frontpage'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
