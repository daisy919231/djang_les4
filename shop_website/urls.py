from django.contrib import admin
from django.urls import path
from shop_website import views
urlpatterns=[
    path('admin/',admin.site.urls),
    path('product-list/', views.product_list, name='product_list'),
    path('category/<int:category_id>/', views.product_list, name='category_detail_id'),
    path('pd/<int:product_id>', views.product_details, name='product_details'),
    path('product/<int:product_id>/add-comment/', views.add_comment, name='add_comment'),
    path('product/<int:product_id>/place-order/', views.place_order, name='place_order')
    


]