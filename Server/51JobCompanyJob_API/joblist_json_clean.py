# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 08:17:52 2020

@author: 81552
"""


import json

company_info_list = []
word_0=''
word_1=''
with open('Server/Data/jobs_list.json','r',encoding='utf-8')as f:
    company_info_list = json.loads(f.read())
    
   
for company in company_info_list:
    for i in range(len(company_info_list[company])):
        
        word_0=company_info_list[company][i][3]#合并经验学历 
        if(word_0.find('人') != -1):
            company_info_list[company][i][1]=company_info_list[company][i][2]+'+'+company_info_list[company][i][1]
            del company_info_list[company][i][2]
            
        word_1=company_info_list[company][i][1]#无经验学历要求
        if(word_1.find('人') != -1):
            company_info_list[company][i].insert(1,'')
with open('Server/Data/company_info_list_clean.json','w',encoding='utf-8')as f:
    f.write(json.dumps(company_info_list, ensure_ascii=False, indent=4))
   
#test
count=0
for company in company_info_list:
    for i in range(len(company_info_list[company])):
        L=(len(company_info_list[company][i]))
        if L!=6:
            count+=1
print(count)
