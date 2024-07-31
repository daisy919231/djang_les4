from django.contrib import admin
from django.urls import path
from shop_website import views
urlpatterns=[
    path('admin/',admin.site.urls),
    path('product-list/', views.product_list, name='product_list'),
    path('pd/<int:product_id>', views.product_details, name='product_details'),


]