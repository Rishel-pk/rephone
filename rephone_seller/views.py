from random import random
from urllib import request
from django.shortcuts import render, redirect
# from .models import *
from django.core.files.storage import FileSystemStorage


def seller_addproduct(request):
    add_pro = request.session['rephone']
    if request.method == 'POST':
        product_name = request.POST['product_name']
        category = request.POST['category']
        quantity = request.POST['ava_quantity']
        description = request.POST['p_description']
        percentage_discount = request.POST['percentage_discount']
        mrp = request.POST['mrp']
        discount_price = request.POST['discount_price']
        image = request.FILES['image']
        image_name = str(random())+image.name
        file = FileSystemStorage()
        file.save(image_name, image)
        add_pro = seller_add_product(product_name=product_name, category=category,Available_quantity=quantity, product_description=description,
                                     percentage_discount=percentage_discount, MRP=mrp, discount_price=discount_price, image=image_name
                                     )
        add_pro.save()                             

    return render(request, 'seller_temp/seller_addproduct.html')


def seller_allproduct(request):
    return render(request, 'seller_temp/seller_allproduct.html')


def seller_manageorder(request):
    return render(request, 'seller_temp/seller_manageorder.html')


def seller_registerView(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        company_name = request.POST["company_name"]
        company_adress = request.POST["company_adress"]
        company_adress_2 = request.POST["company_adress_2"]
        country = request.POST["country"]
        state = request.POST["state"]
        zip = request.POST["zip"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        seller_model = Seller_reg(username=username, email=email, phone=phone, company_name=company_name,
                                  company_adress=company_adress, company_adress_2=company_adress_2,
                                  country=country, state=state, zip=zip, password=password, confirm_password=confirm_password)
        seller_model.save()

        return render(request, 'seller_temp/seller_login.html')

    return render(request, 'seller_temp/seller_register.html')


def seller_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            log = Seller_reg.objects.get(email=email, password=password)
            request.session['rephone'] = log.id
            return redirect('seller_home')
        except Seller_reg.DoesNotExist:
            return render(request, 'seller_temp/seller_login.html', {'lg': 'wrong password'})
    return render(request, 'seller_temp/seller_login.html')


def seller_logout(request):
    del request.session['rephone']
    return redirect('seller_login')


def seller(request):
    return render(request, 'seller_temp/sellermaster.html')
