from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('shorten/', views.shorten_url, name='shorten_url'),
    path('retrieve/', views.retrieve_url, name='retrieve_url'),
    path('redirect/<str:short_url>/', views.redirect_original, name='redirect_original'),
    path('<str:short_code>/', views.redirect_original, name='redirect_original'),
    path('shorten/', views.shorten_url, name='shorten_url'),
    
]
