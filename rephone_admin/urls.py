from django.urls import path
from.import views

urlpatterns = [
    path('a',views.das,name='dash'),
    path('a1',views.admin_dash,name='admin_dash'),
    path('a2',views.addpro,name='addpro'),
    path('a3',views.product_list,name='pro_list'),
    path('a4',views.manage_order,name='manage_order'),
    path('login',views.login,name='login')
 



]