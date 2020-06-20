import json
with open('Data/captcha_img_list.json','r',encoding='utf-8')as f:
    captcha_img_list = json.loads(f.read())

newcaptcha_img_list = []

for j in captcha_img_list:
    j.replace('\n','')
    
for i in range(len(captcha_img_list)):
    newcaptcha_img_list.append({"img":captcha_img_list[i]})

with open('Data/newcaptcha_img_list.json','w',encoding='utf-8')as f:
    f.write(json.dumps(newcaptcha_img_list))
print('数据整理完成')
