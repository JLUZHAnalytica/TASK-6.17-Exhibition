# 说明

## insert_jobs_to_db.py

需要用命令行创建一个新的数据库job51，用代码不好实。

用命令行打开到mongodb bin目录->运行mongo.exe->use job51->db.job51.insert({"随便写点啥":"随便写点啥"})->show dbs

检查是否成功，再运行代码。

## 51job_flask.py
在服务器运行的api程序，生成的可用api地址：http://121.199.66.40:5000/51job.html?page=1&limit=20
