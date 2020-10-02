from django.shortcuts import render
from .models import Product, Similarity

gender_list = ['M','W']
type_list = ['TOP','BOTTOM']

def index(request):        
    import random
    from random import shuffle
    
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

    items = Product.objects.order_by('?')

    if w != m:
        if w:
            items = Product.objects.filter(gender='W').order_by('?')
        elif m:
            items = Product.objects.filter(gender='M').order_by('?')
    
    if t != b:
        if t:
            items = items.filter(category='TOP').order_by('?')
        elif b:
            items = items.filter(category='BOTTOM').order_by('?')
    
    context = {
        'prod_object':items[:50]
    }
    
    return render(request,'index.html', context)

def sub(request, prod_pk):

    items = Similarity.objects.filter(target_prod=prod_pk)[:33]

    context={
        'target':items[0],
        'items':items[1:]
    }

    return render(request,'sub.html',context)