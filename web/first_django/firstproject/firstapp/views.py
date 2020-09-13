from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Comment,Favorite,User

# Create your views here.

def index(request):    
    products=Product.objects.all()

    context={
        'products':products
    }

    return render(request,'index.html',context)