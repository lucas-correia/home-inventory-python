from unicodedata import name
from django.urls import include, path
from inventory import productView
from inventory import shelfView

urlpatterns = [
                path('products/', productView.list_products, name='list-products'),
                path('products/<reference>/', productView.product_detail_reference, name='get-product-reference'),
                path('shelfs/', shelfView.list_shelfs, name='list-shelfs'),
                path('shelfs/<id>/', shelfView.shelf_detail_id, name='get-shelf-id')
                ]