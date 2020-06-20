# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author；鸿
'''数据整理'''
import json
with open('company_info_list.json','r',encoding='utf-8')as f:
    company_info_list = json.loads(f.read())

newcompany_info_list = []
for company in company_info_list:
    newcompany = []
    newcompany.append(company[0])
    if len(company[1:-4])>=2:
        newcompany.append(' · '.join(company[1:-4]))
    else:
        newcompany.append(company[1])
    newcompany.append(company[-4])
    newcompany.append(company[-3])
    newcompany.append(company[-2])
    newcompany.append(company[-1][0][0])
    newcompany.append(company[-1][1][0])
    newcompany.append(company[-1][2][0])
    newcompany_info_list.append({"com_name":newcompany[0],"com_attribute":newcompany[1],"com_city":newcompany[2],"com_trade":newcompany[3],"com_url":newcompany[4],"com_info":newcompany[5],"com_address":newcompany[6],"com_web":newcompany[7]})

with open('newcompany_info_list.json','w',encoding='utf-8')as f:
    f.write(json.dumps(newcompany_info_list))