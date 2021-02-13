from django.urls import path
from .import views

app_name = 'produits'

urlpatterns = [
    path('products/',views.product_list, name='product_list'),
    path('search/', views.search, name='Search'),
    path('<category_slug>/',views.product_list, name='product_list_by_category'),
    path('<id>/<slug:slug>/',views.product_detail, name='product_detail'),
]