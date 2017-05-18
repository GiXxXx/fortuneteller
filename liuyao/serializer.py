from rest_framework import serializers
from .models import Bagua
from .models import Liushisigua
from .models import Dizhi
from .models import Wuxing
from .models import Liuqin
from .models import Huntianjiazi


class BaguaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bagua
        fields = ('url', 'gua', 'fangwei', 'qinshu', 'yuzhou', 'yinyang', 'wuxing', 'guaxiang')