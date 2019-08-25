from django.db import models
from tinymce.models import HTMLField
# Create your models here.
class GoodsTest(models.Model):
    '''测试模型类'''
    STATUS_CHICES = (
        (0, '下架'),
        (1, '上架')
    )
    status = models.SmallIntegerField(choices=STATUS_CHICES, verbose_name='商品状态')
    detail = HTMLField(verbose_name='商品详情')

    class Meta:
        db_table = 'df_goods_test'