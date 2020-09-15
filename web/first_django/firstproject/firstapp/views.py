from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Comment,Favorite,User

# Create your views here.


# 랜덤된 이미지를 보여준다
# 메인페이지
def index(request):        
    
    products=Product.objects.all()
    
    context={
        'products':products
    }

    return render(request,'index.html',context)



# 관련된 이미지를 보여준다
# 서브페이지
def sub(request):

    products=Product.objects.all()
    
    context={
        'products':products
    }

    return render(request,'sub.html',context)