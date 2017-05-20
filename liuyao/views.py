# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.generics import RetrieveAPIView
from .models import Bagua
from .models import Liushisigua
from .models import Dizhi
from .models import Wuxing
from .models import Liuqin
from .models import Liushen
from .models import Huntianjiazi
from .models import Yao
from .serializer import YaoSerializer
from .serializer import BaguaSerializer
from .serializer import LiushisiguaSerializer
from.boxcalender import BoxCalender

# Create your views here.
class PaipanInput(RetrieveAPIView):
    renderer_classes = (TemplateHTMLRenderer,)
    def get(self, request):
        template = 'liuyao/index.html'
        yao = {
            'yaoSet': Yao.objects.all(),
            'nameSet': [
                {'label': u'六爻', 'name': 'liuyao', 'time': 1},
                {'label': u'五爻', 'name': 'wuyao', 'time': 2},
                {'label': u'四爻', 'name': 'siyao', 'time': 3},
                {'label': u'三爻', 'name': 'sanyao', 'time': 4},
                {'label': u'二爻', 'name': 'eryao', 'time': 5},
                {'label': u'初爻', 'name': 'chuyao', 'time': 6}
            ]
        }
        return Response(yao, template_name=template)

# def test(request, id):
#     try:
#         bagua = Bagua.objects.get(pk=id)
#     except Bagua.DoesNotExist:
#         raise Http404("Bagua does not exist")
#     return render(request, 'liuyao/index.html', context)


class PaipanResult(APIView):
    def post(self, request):
        gua_image = self.get_gua_image(request)
        return Response(self.get_gua(request, gua_image))

    def get_gua_image(self, request):
        yao_positions_for_nei_gua = ['chuyao', 'eryao', 'sanyao']
        yao_positions_for_wai_gua = ['siyao', 'wuyao', 'liuyao']
        coin_set = request.data
        nei_gua_image = self.build_gua(yao_positions_for_nei_gua, coin_set)
        wai_gua_image = self.build_gua(yao_positions_for_wai_gua, coin_set)
        return {
            'neigua':nei_gua_image,
            'waigua':wai_gua_image
        }

    def build_gua(self, yao_positions, coin_set):
        ben_gua = ""
        bian_gua = ""
        yao_set = Yao.objects.all()
        yao_serializer = YaoSerializer(yao_set, many=True)
        for position in yao_positions:
            for yao in yao_serializer.data:
                if yao['yao'] == coin_set[position]:
                    ben_gua += yao['image']
                    if yao['dong']:
                        bian_gua += yao['reverse']
                    else:
                        bian_gua += yao['image']
        return {
            'bengua': ben_gua,
            'biangua': bian_gua
        }

    def get_gua(self, request, guaImage):
        bengua_neigua_image = guaImage['neigua']['bengua']
        bengua_waigua_image = guaImage['waigua']['bengua']
        biangua_neigua_image = guaImage['neigua']['biangua']
        biangua_waigua_image = guaImage['waigua']['biangua']

        bengua_neigua = Bagua.objects.filter(guaxiang=bengua_neigua_image).first()
        bengua_waigua = Bagua.objects.filter(guaxiang=bengua_waigua_image).first()
        biangua_neigua = Bagua.objects.filter(guaxiang=biangua_neigua_image).first()
        biangua_waigua = Bagua.objects.filter(guaxiang=biangua_waigua_image).first()

        # 获得六十四卦的本卦信息
        bengua = LiushisiguaSerializer(Liushisigua.objects.filter(neigua=bengua_neigua.gua)
                                       .filter(waigua=bengua_waigua.gua).
                                       first()).data
        # 获得六十四卦的变卦信息
        biangua = LiushisiguaSerializer(Liushisigua.objects.filter(neigua=biangua_neigua.gua)
                                        .filter(waigua=biangua_waigua.gua)
                                        .first()).data
        # 附上卦的卦形信息
        bengua['guaxiang'] = bengua_waigua_image + bengua_waigua_image
        biangua['guaxiang'] = biangua_waigua_image + biangua_waigua_image

        # 获得卦属于的宫
        gong = bengua['gong']

        # 获得六十四卦的首宫卦信息
        shougonggua = LiushisiguaSerializer(Liushisigua.objects.filter(neigua=gong)
                                        .filter(waigua=gong)
                                        .first()).data

        # 获得卦的宫位五行
        wuxing = Bagua.objects.filter(gua=gong).first().wuxing

        # 获得五行六亲的mapper
        wuxing_set = Wuxing.objects.filter(wuxing=wuxing).first()
        liuqin_set = Liuqin.objects.filter(liuqin=u"兄弟").first()
        wuxing_liuqin_mapper = {
            wuxing_set.wuxing: liuqin_set.liuqin,
            wuxing_set.sheng: liuqin_set.sheng,
            wuxing_set.ke: liuqin_set.beike,
            wuxing_set.beisheng: liuqin_set.beisheng,
            wuxing_set.beike: liuqin_set.beike
        }

        self.put_wuxing_liuqin_dizhi(bengua, bengua_neigua.gua, bengua_waigua.gua, wuxing, wuxing_liuqin_mapper)
        self.put_wuxing_liuqin_dizhi(biangua, biangua_neigua.gua, biangua_waigua.gua, wuxing, wuxing_liuqin_mapper)
        self.put_wuxing_liuqin_dizhi(shougonggua, gong, gong, wuxing, wuxing_liuqin_mapper)

        self.put_month_day(request, bengua)

        self.put_liushen(bengua)

        return {
            'bengua': bengua,
            'biangua': biangua,
            'shougonggua': shougonggua
        }

    def put_wuxing_liuqin_dizhi(self, gua, gua_neigua, gua_waigua, wuxing, wuxing_liuqin_mapper):
        # 放入卦的宫位五行
        gua['wuxing'] = wuxing

        # 获得卦的各爻地支
        gua_neigua_dizhi = Huntianjiazi.objects.filter(gua=gua_neigua).filter(neiwai=u"内").first()
        gua_waigua_dizhi = Huntianjiazi.objects.filter(gua=gua_waigua).filter(neiwai=u"外").first()

        gua['liuyao_dizhi'] = gua_waigua_dizhi.san
        gua['wuyao_dizhi'] = gua_waigua_dizhi.er
        gua['siyao_dizhi'] = gua_waigua_dizhi.chu
        gua['sanyao_dizhi'] = gua_neigua_dizhi.san
        gua['eryao_dizhi'] = gua_neigua_dizhi.er
        gua['chuyao_dizhi'] = gua_neigua_dizhi.chu

        dizhi_name_set = ['liuyao_dizhi', 'wuyao_dizhi', 'siyao_dizhi', 'sanyao_dizhi', 'eryao_dizhi',
                          'chuyao_dizhi']
        wuxing_name_set = ['liuyao_wuxing', 'wuyao_wuxing', 'siyao_wuxing', 'sanyao_wuxing', 'eryao_wuxing',
                           'chuyao_wuxing']
        liuqin_name_set = ['liuyao_liuqin', 'wuyao_liuqin', 'siyao_liuqin', 'sanyao_liuqin', 'eryao_liuqin',
                           'chuyao_liuqin']

        # 获得卦的各爻五行六亲
        for i in range(0, 6):
            gua[wuxing_name_set[i]] = Dizhi.objects.filter(dizhi=gua[dizhi_name_set[i]]).first().wuxing
            gua[liuqin_name_set[i]] = wuxing_liuqin_mapper[gua[wuxing_name_set[i]]]

        return

    def put_month_day(self, request, bengua):
        date = request.data['date']
        year = date[0:4]
        month = date[5:7]
        day = date[8:10]
        ganzhi = BoxCalender().day(int(year),int(month),int(day))
        bengua['yuezhi'] = ganzhi['yuezhi']
        bengua['rizhi'] = ganzhi['rizhi']
        bengua['rigan'] = ganzhi['rigan']
        return

    def put_liushen(self, gua):
        liushen_set = Liushen.objects.filter(rigan=gua['rigan']).first()
        gua['liuyao_liushen'] = liushen_set.liuyao
        gua['wuyao_liushen'] = liushen_set.wuyao
        gua['siyao_liushen'] = liushen_set.siyao
        gua['sanyao_liushen'] = liushen_set.sanyao
        gua['eryao_liushen'] = liushen_set.eryao
        gua['chuyao_liushen'] = liushen_set.chuyao
        return



