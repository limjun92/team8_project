from ..models import Product, Similarity
import csv
import glob
import os
import sys

def get_dataset():
    cnt = 0
    with open('../../RunUP_dataset/final_W_B.csv',encoding='UTF-8') as csvfile:
        rdr = csv.DictReader(csvfile)
        for i in rdr:
            Product.objects.create(prod_id=cnt,link=i['href'],gender=i['gender'],category=i['type'],image=i['image'],brand=i['brand_name'],price=i['price'])
            cnt+=1
    with open('../../RunUP_dataset/final_M_B.csv',encoding='UTF-8') as csvfile:
        rdr = csv.DictReader(csvfile)
        for i in rdr:
            Product.objects.create(prod_id=cnt,link=i['href'],gender=i['gender'],category=i['type'],image=i['image'],brand=i['brand_name'],price=i['price'])
            cnt+=1
    with open('../../RunUP_dataset/final_M_T.csv',encoding='UTF-8') as csvfile:
        rdr = csv.DictReader(csvfile)
        for i in rdr:
            Product.objects.create(prod_id=cnt,link=i['href'],gender=i['gender'],category=i['type'],image=i['image'],brand=i['brand_name'],price=i['price'])
            cnt+=1
    with open('../../RunUP_dataset/final_W_T.csv',encoding='UTF-8') as csvfile:
        rdr = csv.DictReader(csvfile)
        for i in rdr:
            Product.objects.create(prod_id=cnt,link=i['href'],gender=i['gender'],category=i['type'],image=i['image'],brand=i['brand_name'],price=i['price'])
            cnt+=1

def get_similarity_W_B_():
    for input_file in glob.glob(os.path.join('../../RunUP_dataset/W_B_similarity/','W_B_*')):
            #print(os.path.basename(input_file))
        with open(input_file,encoding='UTF-8') as csvfile:
            rdr = csv.DictReader(csvfile)
            cnt = 0
            for i in rdr:                
                Similarity.objects.create(target_prod=i['target_num'],sim_prod=i['prod_num'],similarity=i['similarity'])
                cnt+=1
                if cnt == 31:
                    break
def get_similarity_M_B_():
    for input_file in glob.glob(os.path.join('../../RunUP_dataset/M_B_similarity/','M_B_*')):
        #print(os.path.basename(input_file))
        with open(input_file,encoding='UTF-8') as csvfile:
            rdr = csv.DictReader(csvfile)
            cnt = 0
            for i in rdr:                
                Similarity.objects.create(target_prod=str(int(i['target_num'])+3657),sim_prod=str(int(i['prod_num'])+3657),similarity=i['similarity'])
                cnt+=1
                if cnt == 31:
                    break
def get_similarity_M_T_():                
    for input_file in glob.glob(os.path.join('../../RunUP_dataset/M_T_similarity/','M_T_*')):
        #print(os.path.basename(input_file))
        with open(input_file,encoding='UTF-8') as csvfile:
            rdr = csv.DictReader(csvfile)
            cnt = 0
            for i in rdr:                
                Similarity.objects.create(target_prod=str(int(i['target_num'])+5190),sim_prod=str(int(i['prod_num'])+5190),similarity=i['similarity'])
                cnt+=1
                if cnt == 31:
                    break
def get_similarity_W_T_():                
    for input_file in glob.glob(os.path.join('../../RunUP_dataset/W_T_similarity/','W_T_*')):
        #print(os.path.basename(input_file))
        with open(input_file,encoding='UTF-8') as csvfile:
            rdr = csv.DictReader(csvfile)
            cnt = 0
            for i in rdr:
                Similarity.objects.create(target_prod=str(int(i['target_num'])+9675),sim_prod=str(int(i['prod_num'])+9675),similarity=i['similarity'])
                cnt+=1
                if cnt == 31:
                    break