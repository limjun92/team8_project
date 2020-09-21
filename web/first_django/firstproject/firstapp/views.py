from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Comment,Favorite,User

# Create your views here.


# 랜덤된 이미지를 보여준다
# 메인페이지
def index(request):        
    
    answer=request.POST.getlist('check')
    products=Product.objects.all()
    
    context={
        'products':products,
        'answer':answer
    }

    return render(request,'index.html',context)



# 관련된 이미지를 보여준다
# 서브페이지
def sub(request):
    
    import csv
    import pandas as pd
    import random
    # from ssapp.models import Stock

    num = random.randint(0,2125) #수정해야함::index에서 받아오기


    # 유사도 top30 
    with open(f"C:/Users/ssy01/OneDrive/바탕 화면/first_django/firstproject/similarity_v2/{num}_similarity.csv", 'r') as f:
        dr = csv.DictReader(f)
        s = pd.DataFrame(dr)

    # 상품 실제 링크와 이미지 가져오기
    with open("C:/Users/ssy01/OneDrive/바탕 화면/first_django/firstproject/W_top_combined.csv", 'r') as f2:
        dr2 = csv.DictReader(f2)
        s2 = pd.DataFrame(dr2)

    target =s2['images'][num]
    details = []

    for i in range(1,31):
        prod_num = int(s['prod_num'][i])
        image = s2['images'][prod_num]
        href = s2['link'][prod_num]
        details.append([href, image])
    
    # for i in range(len(s)):
    #     Stock.objects.create(name=ss[i][0], code=ss[i][1], ipo_date=ss[i][2])
    
    # products=Product.objects.all()
        
    context={
        # 'products':products
        # 'similarity' : ss
        'target' : target,
        'details' : details,
    }
    

    return render(request,'sub.html',context)