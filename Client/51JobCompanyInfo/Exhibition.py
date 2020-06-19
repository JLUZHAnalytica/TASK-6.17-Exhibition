# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author；鸿
import os
from prettytable import PrettyTable
import json
import requests

def get_data(page, limit):
    res = json.loads(requests.get('http://127.0.0.1:5000/company_list?page={}&limit={}'.format(page, limit)).text)
    return res["data"]

def com_ls_page(page,limit):
    os.system('cls')
    x = PrettyTable()
    x.field_names = ["序号","公司名称","公司属性","公司所在城市","公司行业"]#,"公司URL"
    # com_ls = list(company_info_list_collection.find().skip((page-1)*limit).limit(limit))
    com_ls = get_data(page, limit)
    for i in range(limit):
        x.add_row([i+1,com_ls[i]["com_name"],com_ls[i]["com_attribute"],com_ls[i]["com_city"],com_ls[i]["com_trade"]])#,com_ls[i]["com_url"]
    print(x)
    return com_ls

def com_info(i,com_ls):
    os.system('cls')
    print("公司名称：{}\n公司介绍：{}\n公司地址：{}\n公司官网：{}\n".format(com_ls[i-1]["com_name"],com_ls[i-1]["com_info"],com_ls[i-1]["com_address"],com_ls[i-1]["com_web"]))
    input('按下任意键返回...')

def com_ls_page_frist(page,limit = 20):
    os.system('cls')
    x = PrettyTable()
    x.field_names = ["序号","公司名称","公司属性","公司所在城市","公司行业"]#,"公司URL"
    # com_ls = list(company_info_list_collection.find().skip((page-1)*limit).limit(limit))
    com_ls = get_data(page, limit)
    for i in range(limit):
        x.add_row([i+1,com_ls[i]["com_name"],com_ls[i]["com_attribute"],com_ls[i]["com_city"],com_ls[i]["com_trade"]])#,com_ls[i]["com_url"]
    print(x)
    return com_ls

def Menu(page,com_ls,limit=20):
    while True:
        print('欢迎进入天鹰万象团队工作室——51job展示页面！')
        print('1.更换每页展示的个数')
        print('2.选择公司')
        choose = str(input('请选择(按下回车翻页,按下-1退出)：'))
        if choose == '':
            page = page + 1
            com_ls = com_ls_page(page,limit)
        elif choose == '1':
            limit = int(input('请输入个数：'))
            com_ls = com_ls_page(page,limit)
        elif choose == '2':
            click = int(input('请输入公司的序号：'))
            com_info(click,com_ls)
            com_ls_page(page,limit)
        elif choose == '-1':
            break

if __name__ == '__main__':
    # client = MongoClient()
    # company_info_list_collection = client['test-database']['company_list']
    page = 1
    com_ls = com_ls_page_frist(page)#,company_info_list_collection
    Menu(page,com_ls)