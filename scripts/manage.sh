python3 manage.py makemigrations plantcenter # 激活数据表


python3 manage.py migrate   # 创建表结构

python3 manage.py makemigrations TestModel  # 让 Django 知道我们在我们的模型有一些变更
python3 manage.py migrate TestModel   # 创建表结构