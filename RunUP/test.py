import csv
from recommendapp.models import *

hand = open('M_bottom_combined.csv')
reader = csv.reader(hand)
next(reader,None)
bulk_list = []
for row in reader:
    bulk_list.append(Product(
        prod_id = row[2]+row[3][0]+row[0],
        link=row[1],
        gender=row[2],
        category=row[3],
        image=row[4]))
print(bulk_list)
Product.objects.bulk_create(bulk_list)
Product.objects.values()



import csv
from recommendapp.models import *

for i in range(1810):
    hand = open(f'C:/Users/ssy01/OneDrive/바탕 화면/similarity_v2/M_BOTTOM/{i}_similarity.csv')
    reader = csv.reader(hand)
    next(reader,None)
    
    cnt=0
    for row in reader:
        Similarity.objects.update_or_create(target_prod = Product.objects.get(prod_id='MB'+str(i+1)),sim_prod = Product.objects.get(prod_id='MB'+str(int(row[2])+1)),similarity=float(row[1]))
        cnt+=1
        if cnt>50:break