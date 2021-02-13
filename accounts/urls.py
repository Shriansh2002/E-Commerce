from django.urls import path
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views

from products import views as products_views
from . import views

app_name = 'accounts'


urlpatterns = [
    path('', products_views.product_list, name='home'),
    path('accounts/register/',views.UserFormView.as_view(), name='register'),
    path('accounts/login/', views.LoginView.as_view(),
         {'template_name': 'registration/login.html'}, name='login'),
    path('accounts/logout/', views.logoutView.as_view(), name ='logout'),

    path('accounts/profile/', views.ProfileUpdate.as_view(
        template_name='registration/profile.html', success_url="."), name='profile'),

]+ static(settings.STATIC_URL, document_root = settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
