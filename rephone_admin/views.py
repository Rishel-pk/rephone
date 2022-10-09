from django.shortcuts import render

def das (request):
    return render(request,'admintemp/dashboard.html')

def admin_dash (request):
    return render (request,'admintemp/admin_dash.html')  

def addpro (request):
    return render (request,'admintemp/addproduct.html')    

def product_list (request):
    return render (request,'admintemp/products_list.html')        

def manage_order (request):
    return render (request,'admintemp/manageorder.html')        



def login (request):
    return render (request,'admintemp/login.html')    
          




 