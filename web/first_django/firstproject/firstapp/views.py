from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Comment,Favorite,User

# Create your views here.

def get_db():
    products=Product.objects.all()
    context={
        'products':products
    }
    return context



def index(request):        
    
    products=Product.objects.all()
    
    context={
        'products':products
    }

    return render(request,'index.html',context)


def check(request):
    print('function check')
    answer=request.POST.getlist('check')
    products=Product.objects.all()
    print(answer)
    context={
        'products':products,
        'answers':answer
    }
    answer=get_db
    for i in products:
        print(i)   


    return render(request,'index.html',context)

def sub(request):
    return render(request,'sub.html')