from rest_framework import serializers
# from .models import Bagua
# from .models import Liushisigua
# from .models import Dizhi
# from .models import Wuxing
# from .models import Liuqin
# from .models import Huntianjiazi
# from .models import Yao
#
#
# class BaguaSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Bagua
#         fields = ('gua', 'fangwei', 'qinshu', 'yuzhou', 'yinyang', 'wuxing', 'guaxiang')
#
#
# class YaoSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Yao
#         fields = ('yao', 'coin', 'name', 'image', 'dong', 'reverse')
#
# class LiushisiguaSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Liushisigua
#         fields = ('xu', 'gua', 'gong', 'waigua', 'neigua', 'shi', 'ying', 'liuchong',
#                   'liuhe', 'youhun', 'guihun')