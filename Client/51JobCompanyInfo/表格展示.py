# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 22:01:42 2020

@author: Y
"""
from prettytable import PrettyTable
import json
import requests

def get_data(page, limit):
    data = json.loads(requests.get('http://121.199.66.40:5000/51job.html?page={}&limit={}'.format(page, limit)).text)
    x = PrettyTable()
    x.field_names = ["id","company","Name","Experience","Degree","Need","Area","Salary","URL"]#,"公司URL"
    for i in data["data"]:
        x.add_row([i['id'],i['company'],i['Name'],i['Experience'],i['Degree'],i['Need'],i['Area'],'Salary',i['URL']])
    print(x)
    print("当前页数为{}页，当前每页个数为{}个".format(page, limit))
    print()

if __name__ == '__main__':
    page=1
    limit=20
    get_data(page, limit)
    while(True):
        print("请选择：1.查看下一页，2.跳转到指定页，3.设置每页个数，4.根据id查看信息，5.退出")
        select=input()
        if(select=="1"):
            page+=1
            get_data(page, limit)
        elif(select=="2"):
            page=input("请输入页数")
            get_data(page, limit)
        elif(select=="3"):
            limit=input("情输入个数")
            get_data(page, limit)
        elif(select=="4"):
            page=int(input("请输入要查看的公司id"))
            limit=1
            get_data(page+1, limit)
        elif(select=="5"):
            print("已退出")
            break
        else:
            print("错误请求，请重新选择")

