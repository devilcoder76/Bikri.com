import products
import json
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db.models import Q
from .models import product,orders
from users.models import userdata

def sample(request):
    return HttpResponse("Product view Working:-")

def view_products(request):
    product_items=product.objects.all()
    search_item=request.GET.get('search_item')
    if search_item!='' and search_item is not None:
        product_items=product.objects.filter(title__icontains=search_item)
    if request.session.has_key('id'):
        return render(request,'products/view_product.html',{'product_items':product_items,'status':True,'user_type':request.session['type']})
    return render(request,'products/view_product.html',{'product_items':product_items})

def sell_product(request):
    if request.session.has_key('id'):
        user=userdata.objects.get(id=request.session['id'])
        print(user.user_type)
        if user.user_type=="2":
            if request.method=="POST":
                title=request.POST.get('title')
                desc=request.POST.get('desc')
                price=request.POST.get('price')
                image=request.FILES.get('image')
                new_product=product(seller_id=request.session['id'],title=title,desc=desc,price=price,image=image)
                new_product.save()
                return redirect('products:view_product')
            return render(request,'products/sell.html',{'status':True,'user_type':request.session['type']})
        return HttpResponse('Please create a seller account')
    return HttpResponse('Log In First:')
    
def cart_view(request):
    data=[]
    if request.method=="POST":
        cart_items=json.loads(request.POST.get('cart'))
        print(cart_items)
        for i in cart_items:
            data.append(product.objects.get(id=int(i)))
    if request.session.has_key('id'):
       return render(request,"products/cart.html",{'products':data,'status':True,'user_type':request.session['type'],"cart_disable":True})

def seller_orders(request):
    products=product.objects.filter(seller_id=request.session['id'])
    data=[]
    for i in products:
        data.append(orders.objects.filter(product_id=i.id))
    print(data)
    return render(request,'products/sell_orders.html',{'data':data,'status':True,'user_type':request.session['type']})

def view_product_single(request,pk):
    product_item=product.objects.get(id=pk)
    if request.session.has_key('id'):
        return render(request,"products/product.html",{'data':product_item,'status':True,'user_type':request.session['type']})
    return render(request,"products/product.html",{'data':product_item})

def order_product(request,pk):
    if request.session.has_key('id'):
        if request.method=="POST":
            qty=request.POST.get('qty')
            if qty!='' and qty is not None:
                new_order=orders(customer_id=request.session['id'],product_id=pk,qty=qty)
                new_order.save()
                return render(request,'products/order_success.html',{'status':True,'user_type':request.session['type']})    
        product_item=product.objects.get(id=pk)
        return render(request,"products/order.html",{'data':product_item,'status':True,'user_type':request.session['type']})

def view_orders(request):
    if request.session.has_key('id'):
        all_orders=orders.objects.filter(customer_id=request.session['id'])
        products=[]
        
        for i in all_orders:
            data1=product.objects.get(id=i.product_id)
            data2={}
            data2['qty']=i.qty
            data2['date_time']=i.date_time
            products.append([data1,data2])
        return render(request,'products/view_orders.html',{'products':products,'status':True,'user_type':request.session['type']})

def view_listed_products(request):
    if request.session.has_key('id') and request.session['type']=="2":
        all_products=product.objects.filter(seller_id=request.session['id'])
        return render(request,'products/seller_view.html',{'all_products':all_products,'status':True,'user_type':request.session['type']})
    