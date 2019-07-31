from django.urls import path
from . import views

urlpatterns = [

	path('',views.home, name='home'),
    path('auth/', views.auth, name='auth'),
    path('exit/', views.exit, name='exit'),
    path('chR/', views.chr, name='chr'),
    path('chU/', views.chu, name='chu'),
    path('auth/reg/', views.reg, name='reg'),

    ]