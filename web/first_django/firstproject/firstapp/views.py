from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Comment,Favorite,User
    
import csv
import pandas as pd
import random
# Create your views here.
gender_list = ['M','W']
type_list = ['TOP','BOTTOM']

# 랜덤된 이미지를 보여준다
# 메인페이지
def index(request):        
    
    answer=request.POST.getlist('check')
    
    w, m, t, b = 0, 0, 0, 0 

    if 'Woman' in answer:
        w = 1
    if 'Man' in answer:
        m = 1
    if 'top' in answer:
        t = 1
    if 'bottoms' in answer:
        b = 1

    with open("C:/Users/ssy01/OneDrive - 고려대학교/인공지능사관학교/TEAM8/team8_project/ssy/dataset/all_combined.csv", 'r') as f2:
        dr2 = csv.DictReader(f2)
        s2 = pd.DataFrame(dr2)
    
    if w != m:
        if w:
            s2 = s2[s2.gender == 'W']
        else:
            s2 = s2[s2.gender == 'M']

    if t != b:
        if t:
            s2 = s2[s2.type == 'TOP']
        else:
            s2 = s2[s2.type == 'BOTTOM']
             
    details = []
    nums = random.sample(range(len(s2)),100)
    for num in nums:
        link, gender, type_, image, idx = s2.iloc[num]  
        prod_num = str(gender_list.index(gender)) + str(type_list.index(type_)) + str(idx)
        details.append([prod_num, image])
    
    context = {
        'products' : details
    }

    return render(request,'index.html',context)



# 관련된 이미지를 보여준다
# 서브페이지
def sub(request, prod_num):


    gender = gender_list[int(prod_num[0])]
    type_ = type_list[int(prod_num[1])]
    prod_num = int(prod_num[2:])

    # 유사도 top30 
    with open(f"C:/Users/ssy01/OneDrive/바탕 화면/similarity_v2/{gender}_{type_}/{prod_num}_similarity.csv", 'r') as f:
        dr = csv.DictReader(f)
        s = pd.DataFrame(dr)

    # 상품 실제 링크와 이미지 가져오기
    with open(f"C:/Users/ssy01/OneDrive - 고려대학교/인공지능사관학교/TEAM8/team8_project/ssy/dataset/{gender}_{type_}_combined.csv", 'r') as f2:
        dr2 = csv.DictReader(f2)
        s2 = pd.DataFrame(dr2)

    target = s2.iloc[prod_num]

    details = []
    for i in range(1,31):
        sub_prod_num = int(s['prod_num'][i])
        image = s2['images'][sub_prod_num]
        href = s2['link'][sub_prod_num]
        details.append([href, image])

        
    context={

        'target' : target,
        'details' : details,
    }
    

    return render(request,'sub.html',context)