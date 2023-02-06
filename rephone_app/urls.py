from django.urls import path
from.import views

urlpatterns = [
    path('m0',views.mas,name='mast') ,
    path('',views.re,name='mob'),
    path('m2',views.android,name='andro'),
    path('m4',views.contact,name='sin'),
    path('m3',views.io,name='io'),
    path('m5',views.cart,name='car'),
    path('m6',views.check,name='checkout'),
    path('m7',views.login,name='login'),
    path('m8',views.rgister,name='register')

   


]


