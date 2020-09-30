import os
import glob
import pandas as pd

# folder_name_list = ['jaramshop','','망고스틴']
# for folder_name in folder_name_list:
#     try:
#         os.chdir(f"C:/Users/ssy01/OneDrive - 고려대학교/인공지능사관학교/3_인공지능서비스프로젝트/scraping/스마트스토어/{folder_name}")

#     except:
#         print('##find error##',folder_name)
#         continue

#     extension = 'csv'
#     all_filenames = [i for i in glob.glob('*_detail.{}'.format(extension))]

#     #combine all files in the list
#     combined_csv = pd.concat([pd.read_csv(f, encoding='cp949', names=['link','prod_id','original_num','name','price','gender','type','images']) for f in all_filenames ])
    
#     #export to csv
#     combined_csv.to_csv(f"{folder_name}_detail_combined.csv", index=False, encoding='utf-8-sig')


extension = 'csv'
all_filenames = [i for i in glob.glob('nike_W_B_*.{}'.format(extension))]

#combine all files in the list
# try:
#     combined_csv = pd.concat([pd.read_csv(f, encoding='cp949', names=['link','prod_id','original_num','name','price','gender','type','images']) for f in all_filenames ])
# except:
combined_csv = pd.concat([pd.read_csv(f, encoding='utf-8') for f in all_filenames ])

#export to csv
combined_csv.to_csv(f"nike_W_B.csv", index=False)
