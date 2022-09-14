from django.urls import path
from.import views

urlpatterns = [
    path('m0',views.mas,name='mast') ,
    path('m1',views.re,name='mob'),
    path('m2',views.android,name='andro'),
    path('m4',views.contact,name='sin'),
    path('m3',views.io,name='io'),
    path('m5',views.cart,name='car')

   


]


