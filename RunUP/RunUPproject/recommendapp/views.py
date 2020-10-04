from django.shortcuts import render
from .models import Product, Similarity
from recommendapp.module.get_csv import get_dataset, get_similarity_W_T_, get_similarity_M_T_, get_similarity_M_B_, get_similarity_W_B_
gender_list = ['M','W']
type_list = ['TOP','BOTTOM']

def index(request):        
    import random
    from random import shuffle

    cnt = 0

    if not Product.objects.filter(prod_id=cnt).exists():
        get_dataset()
    if not Similarity.objects.filter(target_prod=0).exists():
        get_similarity_W_T_()
        get_similarity_M_T_()
        get_similarity_M_B_()
        get_similarity_W_B_()


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
    print('prod_pk',prod_pk)
    items = Similarity.objects.filter(target_prod=prod_pk)[:31]
    #print(items)

    for item in items:
        print('target_prod',item.target_prod)
        break

    content = []
    main = {}
    #print(items[0].target_product)
    #print(items[0].sim_product)
    check = True
    for item in items:
        if check:
            main = {'img':item.sim_product.image,'href':item.sim_product.link,'brand':item.sim_product.brand,'price':item.sim_product.price,'prod_id':item.sim_product.prod_id}
            check = False
            continue
        content.append({'img':item.sim_product.image,'href':item.sim_product.link,'brand':item.sim_product.brand,'price':item.sim_product.price,'prod_id':item.sim_product.prod_id})
    # print(images)
    context={
        #'target':items[0],
        'main':main,
        'contents':content,
    }

    return render(request,'sub.html',context)