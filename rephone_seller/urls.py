from django.urls import path
from.import views


urlpatterns = [
path('',views.seller,name='seller_home'),
path('s1',views.seller_addproduct,name='seller_add'),
path('s2',views.seller_allproduct,name='seller_all'),
path('s3',views.seller_manageorder,name='seller_manage'),
path('s4',views.seller_registerView,name='seller_reg'),
path('s5',views.seller_login,name='seller_login'),
path('s6',views.seller_logout,name='seller_logout')
]