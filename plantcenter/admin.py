from django.contrib import admin

# Register your models here.
from .models import PlantStatus

admin.site.site_header = '植物数据中心'
admin.site.site_title = '植物数据中心'
admin.site.index_title = u'植物数据中心'

class PlantStatusAdmin(admin.ModelAdmin):

    list_display = ('device', 'date',  'time', 'light','temperature','humidity')
    list_filter = ('device', 'date', 'time',)
    search_fields = ('device','email') # 添加快速查询栏
    list_per_page = 100

    # '''设置可编辑字段'''
    # list_editable = ('status',)

    # '''按日期月份筛选'''
    # date_hierarchy = 'date'

    # '''按发布日期排序'''
    # ordering = ('-date',)
    empty_value_display = "/"

admin.site.register(PlantStatus,PlantStatusAdmin)