from prettytable import PrettyTable
import json
#读取数据
#文件为绝对路径。
with open('C:\DLR\dlr-workplace\项目\数据样式(1) - 副本.json','r+',encoding='utf-8') as ifo:
    ls=ifo.read()
    data=json.loads(ls)#注意json文件中1.'改为";2.文件中字典间的逗号。
    tb=PrettyTable()

#制表    
    tb.field_names = ["name", "attribute", "city", "trade","id"]
    for i in range(len(data)):
        tb.add_row([data[i]["com_name"],data[i]["com_attribute"],data[i]["com_city"],data[i]["com_trade"],i+1])
    print(tb)    
