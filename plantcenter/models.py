from django.db import models

# Create your models here.
"""
models.CharField   		用来存储字符串，必须制定范围
models.AutoField   		根据可用id自动递增的整数字段。通常不需要直接使用它;如果不指定主键字段，则会自动将主键字段添加到模型中 
models.DateField   		使用Python的datetime.date实例保存的日期。auto_now = True:每次保存对象时，自动设置该字段为当前时间;auto_now_add=True:对象第一次被创建时自动设置当前时间。需要注意的是，自动保存的时间的时区使用的是默认时区。
models.DateTimeField    使用Python的datetime.datetime实例表示的日期和时间
models.TextField        存储大字符串
models.BooleanField     该字段的默认表单控件是CheckboxInput，如果你需要设置null 值，则使用NullBooleanField 来代替BooleanField
models.FloatField   	用Python的一个float 实例来表示一个浮点数。
models.ForeignKey       多对一关系
models.ManyToManyField  多对多关联
models.OneToOneField    一对一关联关系

1、null=True            数据库字段可以为空
2、blank=True           django的 Admin 中添加数据时是否可允许空值
3、primary_key = False  主键，对AutoField设置主键后，就会代替原来的自增 id 列
如果您没有为模型中的任何字段指定primary_key=True, Django将自动添加一个IntegerField来保存主键，所以您不需要在任何字段上设置primary_key=True，除非您想要覆盖默认的主键行为
4、auto_now             自动创建 无论添加或修改，都是当前操作的时间
5、auto_now_add         自动创建 永远是创建时的时间
6、max_length           字符串最大长度
7、default              默认值
8、verbose_name         Admin中字段的显示名称
9、unique=True          不允许重复
10、db_index = True     数据库索引
11、auto_created=False  自动创建
12、help_text           字段注释


"""


class PlantStatus(models.Model):
    class Meta:
        db_table = 'plantstatus'    # 数据库中显示的表的名称
        verbose_name = '植物状态'
        verbose_name_plural = verbose_name

    id = models.AutoField(primary_key=True)
    device = models.IntegerField(verbose_name='设备编号',null=False)
    date = models.DateField(verbose_name='日期',null=False)
    time = models.TimeField(verbose_name='时间',null=False)
    # date=
    light = models.FloatField(verbose_name='光线',null=True)
    temperature = models.FloatField(verbose_name='温度',null=True)
    humidity = models.FloatField(verbose_name='湿度',null=True)
