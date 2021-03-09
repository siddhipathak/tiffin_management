from django.http import HttpResponse
from django.shortcuts import render
from .models import Product, Order
from math import ceil
import logging

logger = logging.getLogger(__name__)

def index(request):
    # all_products = []
    category_prod = Product.objects.all()
    # cats = {item['category'] for item in category_prod}
    # for cat in cats:
    #     prod = Product.objects.filter(category=cat)
    #     n = len(prod)
    #     nSlides = n // 4 + ceil((n / 4) - (n // 4))
    #     all_products.append([prod, range(1, nSlides), nSlides])
    # params = {'all_products': all_products}
    return render(request, "shop/index.html", {'category_prod': category_prod})

def searchMatch(query,item):
    if query in item.description.lower() or query in item.product_name.lower() or query in item.category.lower():
        return True
    else:
        return False

# def search(request):
#     query = request.GET.get('search')
#     allprod = []
#     params = Product.objects.values('category', 'id')
#     cats = {item['category'] for item in params}
#     for cat in cats:
#         prodtemp = Product.objects.filter(category=cat)
#         prod = [item for item in prodtemp if searchMatch(query, item)]
#         if len(prod)!= 0:
#             allprod.append(prod)
#     category_prod = {'category_prod': allprod}
#     for i in allprod:
#         print(i.id)
#         print(i.description)
#     return render(request, "shop/index.html", category_prod)

def search(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        post = Product.objects.all().filter(product_name__contains=search)
        print(post)
        return render(request, "shop/index.html", {'category_prod': post})

def about(request):
    return render(request, "shop/about.html")

def tracker(request):
    return render(request, "shop/tracker.html")



def productview(request,myid):
    product = Product.objects.filter(id=myid)
    print(product)
    return render(request, "shop/prodview.html", {'productf': product[0]})

def checkout(request):
    if request.method == "POST":
        items_json = request.POST.get('itemsJson', '')
        meal_duration = request.POST.get('meal_duration', '')
        no_of_meal = request.POST.get('no_of_meal', '')
        quantity_meal = request.POST.get('quantity_meal', '')
        meal_total = request.POST.get('meal_total', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        address = request.POST.get('address1', '')+" "+request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        order = Order(items_json=items_json, meal_duration=meal_duration, no_of_meal=no_of_meal, quantity_meal=quantity_meal, meal_total=meal_total, name=name, email=email, phone=phone, address=address, city=city, state=state, zip_code=zip_code)
        order.save()
        thank = True
        id = order.order_id
        return render(request, 'shop/checkout.html', {'thank': thank, 'id': id})
    return render(request, 'shop/checkout.html')

def prodview1(request):
    print(request.POST)
    return render(request, "shop/prodview1.html")






