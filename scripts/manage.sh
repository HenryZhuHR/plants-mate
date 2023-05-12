python3 manage.py makemigrations plantcenter # 激活数据表


python3 manage.py migrate   # 创建表结构

python3 manage.py makemigrations TestModel  # 让 Django 知道我们在我们的模型有一些变更
python3 manage.py migrate TestModel   # 创建表结构

python manage.py collectstatic
# 创建管理员
python3 manage.py createsuperuser \
    --username "henryzhu" \
    --email "296506195@qq.com"

# henryzhu296506