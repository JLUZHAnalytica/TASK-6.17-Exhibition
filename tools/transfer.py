import json

captcha_img_list = []
with open("/Users/yokey/Downloads/AI验证码地址.txt", 'r') as fd:
    for line in fd:
        captcha_img_list.append(line[:-1])

with open("Server/Data/captcha_img_list.json", 'w') as fd:
    fd.write(json.dumps(captcha_img_list,indent=4,ensure_ascii=False))
        