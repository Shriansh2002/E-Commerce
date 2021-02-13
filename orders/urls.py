from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    url(r'^create/$', views.order_create, name='order_create'),
    path('history',views.order_history, name='history'),
    path('history/<id>',views.order_history_list, name='order_list')
]
