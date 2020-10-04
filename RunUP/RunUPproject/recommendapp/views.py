from django.shortcuts import render
from .models import Product, Similarity
import csv
import glob
import os
import sys

gender_list = ['M','W']
type_list = ['TOP','BOTTOM']

def index(request):        
    import random
    from random import shuffle

    cnt = 0

    if not Product.objects.filter(prod_id=cnt).exists():
        with open('../../RunUP_dataset/final_W_B.csv',encoding='UTF-8',mode='rb' ) as csvfile:
            rdr = csv.DictReader(csvfile)
            for i in rdr:
                Product.objects.create(prod_id=cnt,link=i['href'],gender=i['gender'],category=i['type'],image=i['image'],brand=i['brand_name'],price=i['price'])
                cnt+=1
        with open('../../RunUP_dataset/final_M_B.csv',encoding='UTF-8',mode='rb') as csvfile:
            rdr = csv.DictReader(csvfile)
            for i in rdr:
                Product.objects.create(prod_id=cnt,link=i['href'],gender=i['gender'],category=i['type'],image=i['image'],brand=i['brand_name'],price=i['price'])
                cnt+=1
        with open('../../RunUP_dataset/final_M_T.csv',encoding='UTF-8',mode='rb') as csvfile:
            rdr = csv.DictReader(csvfile)
            for i in rdr:
                Product.objects.create(prod_id=cnt,link=i['href'],gender=i['gender'],category=i['type'],image=i['image'],brand=i['brand_name'],price=i['price'])
                cnt+=1
        with open('../../RunUP_dataset/final_W_T.csv',encoding='UTF-8',mode='rb') as csvfile:
            rdr = csv.DictReader(csvfile)
            for i in rdr:
                Product.objects.create(prod_id=cnt,link=i['href'],gender=i['gender'],category=i['type'],image=i['image'],brand=i['brand_name'],price=i['price'])
                cnt+=1
    if not Similarity.objects.filter(target_prod=0).exists():
        for input_file in glob.glob(os.path.join('../../RunUP_dataset/W_B_similarity/','W_B_*')):
            #print(os.path.basename(input_file))
            with open(input_file,encoding='UTF-8',mode='rb') as csvfile:
                rdr = csv.DictReader(csvfile)
                cnt = 0
                for i in rdr:                
                    Similarity.objects.create(target_prod=i['target_num'],sim_prod=i['prod_num'],similarity=i['similarity'])
                    cnt+=1
                    if cnt == 31:
                        break


    answer=request.POST.getlist('check')
    print(request.POST)
    w, m, t, b = 0, 0, 0, 0

    if 'Woman' in answer:
        w = 1
    if 'Man' in answer:
        m = 1
    if 'top' in answer:
        t = 1
    if 'bottoms' in answer:
        b = 1

    items = Product.objects.order_by('?')

    if w != m:
        if w:
            items = Product.objects.filter(gender='woman').order_by('?')
        elif m:
            items = Product.objects.filter(gender='man').order_by('?')
    
    if t != b:
        if t:
            items = items.filter(category='top').order_by('?')
        elif b:
            items = items.filter(category='bottom').order_by('?')
    
    context = {
        'prod_object':items[:50]
    }
    
    return render(request,'index.html',context)

def sub(request, prod_pk):
    #print('prod_pk',prod_pk)
    items = Similarity.objects.filter(target_prod=prod_pk)[:31]


    content = []
    main = {}
    #print(items[0].target_product)
    #print(items[0].sim_product)
    check = True
    for item in items:
        if check:
            main = {'img':item.sim_product.image,'href':item.sim_product.link,'brand':item.sim_product.brand,'price':item.sim_product.price}
            check = False
            continue
        content.append({'img':item.sim_product.image,'href':item.sim_product.link,'brand':item.sim_product.brand,'price':item.sim_product.price})
    # print(images)
    context={
        #'target':items[0],
        'main':main,
        'contents':content,
    }

    return render(request,'sub.html',context)