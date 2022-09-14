from django.shortcuts import render
def mas (request):
    return render(request,'retemp/master.html') 
def re (request):
    return render(request,'retemp/home.html')

def android (request):
    return render(request,'retemp/android.html')

def contact (request):
    return render(request,'retemp/contactus.html')

def io (request):
    return render(request,'retemp/ios.html') 
def cart (request):
    return render(request,'retemp/cart.html')      
   




