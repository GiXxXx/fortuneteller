# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from rest_framework.decorators import APIView
from rest_framework.response import Response
from .models import Bagua
from .models import Liushisigua
from .models import Dizhi
from .models import Wuxing
from .models import Liuqin
from .models import Huntianjiazi
from .models import Yao
from .serializer import YaoSerializer
from .serializer import BaguaSerializer
from .serializer import LiushisiguaSerializer
from.boxcalender import BoxCalender

# Create your views here.
yaoSet = Yao.objects.all()
yao_serializer = YaoSerializer(yaoSet, many=True)

def index(request):
    url = 'liuyao/index.html'
    context = {
        'yao': yaoSet,
    }
    return render(request, url, context)

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
        bengua['wuxing'] = wuxing
        biangua['wuxing'] = wuxing
        shougonggua['wuxing'] = wuxing

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

        # 获得卦的各爻地支
        bengua_neigua_dizhi = Huntianjiazi.objects.filter(gua=bengua_neigua.gua).filter(neiwai=u"内").first()
        bengua_waigua_dizhi = Huntianjiazi.objects.filter(gua=bengua_neigua.gua).filter(neiwai=u"外").first()
        biangua_neigua_dizhi = Huntianjiazi.objects.filter(gua=biangua_neigua.gua).filter(neiwai=u"内").first()
        biangua_waigua_dizhi = Huntianjiazi.objects.filter(gua=biangua_neigua.gua).filter(neiwai=u"外").first()

        bengua_sixth_yao_dizhi = bengua_waigua_dizhi.san
        bengua_fifth_yao_dizhi = bengua_waigua_dizhi.er
        bengua_fourth_yao_dizhi = bengua_waigua_dizhi.chu
        bengua_third_yao_dizhi = bengua_neigua_dizhi.san
        bengua_second_yao_dizhi = bengua_neigua_dizhi.er
        bengua_first_yao_dizhi = bengua_neigua_dizhi.chu

        biangua_sixth_yao_dizhi = biangua_waigua_dizhi.san
        biangua_fifth_yao_dizhi = biangua_waigua_dizhi.er
        biangua_fourth_yao_dizhi = biangua_waigua_dizhi.chu
        biangua_third_yao_dizhi = biangua_neigua_dizhi.san
        biangua_second_yao_dizhi = biangua_neigua_dizhi.er
        biangua_first_yao_dizhi = biangua_neigua_dizhi.chu

        # 获得卦的各爻五行
        bengua_sixth_yao_wuxing = Dizhi.objects.filter(dizhi=bengua_sixth_yao_dizhi).first().wuxing
        bengua_fifth_yao_wuxing = Dizhi.objects.filter(dizhi=bengua_fifth_yao_dizhi).first().wuxing
        bengua_fourth_yao_wuxing = Dizhi.objects.filter(dizhi=bengua_fourth_yao_dizhi).first().wuxing
        bengua_third_yao_wuxing = Dizhi.objects.filter(dizhi=bengua_third_yao_dizhi).first().wuxing
        bengua_second_yao_wuxing = Dizhi.objects.filter(dizhi=bengua_second_yao_dizhi).first().wuxing
        bengua_first_yao_wuxing = Dizhi.objects.filter(dizhi=bengua_first_yao_dizhi).first().wuxing

        biangua_sixth_yao_wuxing = Dizhi.objects.filter(dizhi=biangua_sixth_yao_dizhi).first().wuxing
        biangua_fifth_yao_wuxing = Dizhi.objects.filter(dizhi=biangua_fifth_yao_dizhi).first().wuxing
        biangua_fourth_yao_wuxing = Dizhi.objects.filter(dizhi=biangua_fourth_yao_dizhi).first().wuxing
        biangua_third_yao_wuxing = Dizhi.objects.filter(dizhi=biangua_third_yao_dizhi).first().wuxing
        biangua_second_yao_wuxing = Dizhi.objects.filter(dizhi=biangua_second_yao_dizhi).first().wuxing
        biangua_first_yao_wuxing = Dizhi.objects.filter(dizhi=biangua_first_yao_dizhi).first().wuxing

        # 获得卦的各爻六亲
        bengua_sixth_yao_liuqin = wuxing_liuqin_mapper[bengua_sixth_yao_wuxing]
        bengua_fifth_yao_liuqin = wuxing_liuqin_mapper[bengua_fifth_yao_wuxing]
        bengua_fourth_yao_liuqin = wuxing_liuqin_mapper[bengua_fourth_yao_wuxing]
        bengua_third_yao_liuqin = wuxing_liuqin_mapper[bengua_third_yao_wuxing]
        bengua_second_yao_liuqin = wuxing_liuqin_mapper[bengua_second_yao_wuxing]
        bengua_first_yao_liuqin = wuxing_liuqin_mapper[bengua_first_yao_wuxing]

        biangua_sixth_yao_liuqin = wuxing_liuqin_mapper[biangua_sixth_yao_wuxing]
        biangua_fifth_yao_liuqin = wuxing_liuqin_mapper[biangua_fifth_yao_wuxing]
        biangua_fourth_yao_liuqin = wuxing_liuqin_mapper[biangua_fourth_yao_wuxing]
        biangua_third_yao_liuqin = wuxing_liuqin_mapper[biangua_third_yao_wuxing]
        biangua_second_yao_liuqin = wuxing_liuqin_mapper[biangua_second_yao_wuxing]
        biangua_first_yao_liuqin = wuxing_liuqin_mapper[biangua_first_yao_wuxing]

        # 附上卦的六亲地支五行信息
        bengua['liuyao_liuqin'] = bengua_sixth_yao_liuqin
        bengua['wuyao_liuqin'] = bengua_fifth_yao_liuqin
        bengua['siyao_liuqin'] = bengua_fourth_yao_liuqin
        bengua['sanyao_liuqin'] = bengua_third_yao_liuqin
        bengua['eryao_liuqin'] = bengua_second_yao_liuqin
        bengua['chuyao_liuqin'] = bengua_first_yao_liuqin

        bengua['liuyao_dizhi'] = bengua_sixth_yao_dizhi
        bengua['wuyao_dizhi'] = bengua_fifth_yao_dizhi
        bengua['siyao_dizhi'] = bengua_fourth_yao_dizhi
        bengua['sanyao_dizhi'] = bengua_third_yao_dizhi
        bengua['eryao_dizhi'] = bengua_second_yao_dizhi
        bengua['chuyao_dizhi'] = bengua_first_yao_dizhi

        bengua['liuyao_wuxing'] = bengua_sixth_yao_wuxing
        bengua['wuyao_wuxing'] = bengua_fifth_yao_wuxing
        bengua['siyao_wuxing'] = bengua_fourth_yao_wuxing
        bengua['sanyao_wuxing'] = bengua_third_yao_wuxing
        bengua['eryao_wuxing'] = bengua_second_yao_wuxing
        bengua['chuyao_wuxing'] = bengua_first_yao_wuxing

        biangua['liuyao_liuqin'] = biangua_sixth_yao_liuqin
        biangua['wuyao_liuqin'] = biangua_fifth_yao_liuqin
        biangua['siyao_liuqin'] = biangua_fourth_yao_liuqin
        biangua['sanyao_liuqin'] = biangua_third_yao_liuqin
        biangua['eryao_liuqin'] = biangua_second_yao_liuqin
        biangua['chuyao_liuqin'] = biangua_first_yao_liuqin

        biangua['liuyao_dizhi'] = biangua_sixth_yao_dizhi
        biangua['wuyao_dizhi'] = biangua_fifth_yao_dizhi
        biangua['siyao_dizhi'] = biangua_fourth_yao_dizhi
        biangua['sanyao_dizhi'] = biangua_third_yao_dizhi
        biangua['eryao_dizhi'] = biangua_second_yao_dizhi
        biangua['chuyao_dizhi'] = biangua_first_yao_dizhi

        biangua['liuyao_wuxing'] = biangua_sixth_yao_wuxing
        biangua['wuyao_wuxing'] = biangua_fifth_yao_wuxing
        biangua['siyao_wuxing'] = biangua_fourth_yao_wuxing
        biangua['sanyao_wuxing'] = biangua_third_yao_wuxing
        biangua['eryao_wuxing'] = biangua_second_yao_wuxing
        biangua['chuyao_wuxing'] = biangua_first_yao_wuxing

        self.put_month_day(request, bengua, biangua)

        return {
            'bengua': bengua,
            'biangua': biangua
        }

    def put_wuxing_liuqin_dizhi(self, gua):
        # 获得卦的宫位五行
        wuxing = Bagua.objects.filter(gua=gong).first().wuxing
        bengua['wuxing'] = wuxing
        biangua['wuxing'] = wuxing
        shougonggua['wuxing'] = wuxing

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

        # 获得卦的各爻地支
        bengua_neigua_dizhi = Huntianjiazi.objects.filter(gua=bengua_neigua.gua).filter(neiwai=u"内").first()
        bengua_waigua_dizhi = Huntianjiazi.objects.filter(gua=bengua_neigua.gua).filter(neiwai=u"外").first()
        biangua_neigua_dizhi = Huntianjiazi.objects.filter(gua=biangua_neigua.gua).filter(neiwai=u"内").first()
        biangua_waigua_dizhi = Huntianjiazi.objects.filter(gua=biangua_neigua.gua).filter(neiwai=u"外").first()

        bengua_sixth_yao_dizhi = bengua_waigua_dizhi.san
        bengua_fifth_yao_dizhi = bengua_waigua_dizhi.er
        bengua_fourth_yao_dizhi = bengua_waigua_dizhi.chu
        bengua_third_yao_dizhi = bengua_neigua_dizhi.san
        bengua_second_yao_dizhi = bengua_neigua_dizhi.er
        bengua_first_yao_dizhi = bengua_neigua_dizhi.chu

        biangua_sixth_yao_dizhi = biangua_waigua_dizhi.san
        biangua_fifth_yao_dizhi = biangua_waigua_dizhi.er
        biangua_fourth_yao_dizhi = biangua_waigua_dizhi.chu
        biangua_third_yao_dizhi = biangua_neigua_dizhi.san
        biangua_second_yao_dizhi = biangua_neigua_dizhi.er
        biangua_first_yao_dizhi = biangua_neigua_dizhi.chu

        # 获得卦的各爻五行
        bengua_sixth_yao_wuxing = Dizhi.objects.filter(dizhi=bengua_sixth_yao_dizhi).first().wuxing
        bengua_fifth_yao_wuxing = Dizhi.objects.filter(dizhi=bengua_fifth_yao_dizhi).first().wuxing
        bengua_fourth_yao_wuxing = Dizhi.objects.filter(dizhi=bengua_fourth_yao_dizhi).first().wuxing
        bengua_third_yao_wuxing = Dizhi.objects.filter(dizhi=bengua_third_yao_dizhi).first().wuxing
        bengua_second_yao_wuxing = Dizhi.objects.filter(dizhi=bengua_second_yao_dizhi).first().wuxing
        bengua_first_yao_wuxing = Dizhi.objects.filter(dizhi=bengua_first_yao_dizhi).first().wuxing

        biangua_sixth_yao_wuxing = Dizhi.objects.filter(dizhi=biangua_sixth_yao_dizhi).first().wuxing
        biangua_fifth_yao_wuxing = Dizhi.objects.filter(dizhi=biangua_fifth_yao_dizhi).first().wuxing
        biangua_fourth_yao_wuxing = Dizhi.objects.filter(dizhi=biangua_fourth_yao_dizhi).first().wuxing
        biangua_third_yao_wuxing = Dizhi.objects.filter(dizhi=biangua_third_yao_dizhi).first().wuxing
        biangua_second_yao_wuxing = Dizhi.objects.filter(dizhi=biangua_second_yao_dizhi).first().wuxing
        biangua_first_yao_wuxing = Dizhi.objects.filter(dizhi=biangua_first_yao_dizhi).first().wuxing

        # 获得卦的各爻六亲
        bengua_sixth_yao_liuqin = wuxing_liuqin_mapper[bengua_sixth_yao_wuxing]
        bengua_fifth_yao_liuqin = wuxing_liuqin_mapper[bengua_fifth_yao_wuxing]
        bengua_fourth_yao_liuqin = wuxing_liuqin_mapper[bengua_fourth_yao_wuxing]
        bengua_third_yao_liuqin = wuxing_liuqin_mapper[bengua_third_yao_wuxing]
        bengua_second_yao_liuqin = wuxing_liuqin_mapper[bengua_second_yao_wuxing]
        bengua_first_yao_liuqin = wuxing_liuqin_mapper[bengua_first_yao_wuxing]

        biangua_sixth_yao_liuqin = wuxing_liuqin_mapper[biangua_sixth_yao_wuxing]
        biangua_fifth_yao_liuqin = wuxing_liuqin_mapper[biangua_fifth_yao_wuxing]
        biangua_fourth_yao_liuqin = wuxing_liuqin_mapper[biangua_fourth_yao_wuxing]
        biangua_third_yao_liuqin = wuxing_liuqin_mapper[biangua_third_yao_wuxing]
        biangua_second_yao_liuqin = wuxing_liuqin_mapper[biangua_second_yao_wuxing]
        biangua_first_yao_liuqin = wuxing_liuqin_mapper[biangua_first_yao_wuxing]

        # 附上卦的六亲地支五行信息
        bengua['liuyao_liuqin'] = bengua_sixth_yao_liuqin
        bengua['wuyao_liuqin'] = bengua_fifth_yao_liuqin
        bengua['siyao_liuqin'] = bengua_fourth_yao_liuqin
        bengua['sanyao_liuqin'] = bengua_third_yao_liuqin
        bengua['eryao_liuqin'] = bengua_second_yao_liuqin
        bengua['chuyao_liuqin'] = bengua_first_yao_liuqin

        bengua['liuyao_dizhi'] = bengua_sixth_yao_dizhi
        bengua['wuyao_dizhi'] = bengua_fifth_yao_dizhi
        bengua['siyao_dizhi'] = bengua_fourth_yao_dizhi
        bengua['sanyao_dizhi'] = bengua_third_yao_dizhi
        bengua['eryao_dizhi'] = bengua_second_yao_dizhi
        bengua['chuyao_dizhi'] = bengua_first_yao_dizhi

        bengua['liuyao_wuxing'] = bengua_sixth_yao_wuxing
        bengua['wuyao_wuxing'] = bengua_fifth_yao_wuxing
        bengua['siyao_wuxing'] = bengua_fourth_yao_wuxing
        bengua['sanyao_wuxing'] = bengua_third_yao_wuxing
        bengua['eryao_wuxing'] = bengua_second_yao_wuxing
        bengua['chuyao_wuxing'] = bengua_first_yao_wuxing

        biangua['liuyao_liuqin'] = biangua_sixth_yao_liuqin
        biangua['wuyao_liuqin'] = biangua_fifth_yao_liuqin
        biangua['siyao_liuqin'] = biangua_fourth_yao_liuqin
        biangua['sanyao_liuqin'] = biangua_third_yao_liuqin
        biangua['eryao_liuqin'] = biangua_second_yao_liuqin
        biangua['chuyao_liuqin'] = biangua_first_yao_liuqin

        biangua['liuyao_dizhi'] = biangua_sixth_yao_dizhi
        biangua['wuyao_dizhi'] = biangua_fifth_yao_dizhi
        biangua['siyao_dizhi'] = biangua_fourth_yao_dizhi
        biangua['sanyao_dizhi'] = biangua_third_yao_dizhi
        biangua['eryao_dizhi'] = biangua_second_yao_dizhi
        biangua['chuyao_dizhi'] = biangua_first_yao_dizhi

        biangua['liuyao_wuxing'] = biangua_sixth_yao_wuxing
        biangua['wuyao_wuxing'] = biangua_fifth_yao_wuxing
        biangua['siyao_wuxing'] = biangua_fourth_yao_wuxing
        biangua['sanyao_wuxing'] = biangua_third_yao_wuxing
        biangua['eryao_wuxing'] = biangua_second_yao_wuxing
        biangua['chuyao_wuxing'] = biangua_first_yao_wuxing

    def put_month_day(self, request, bengua, biangua):
        date = request.data['date']
        year = date[0:4]
        month = date[5:7]
        day = date[8:10]
        ganzhi = BoxCalender().day(int(year),int(month),int(day))
        bengua["yuezhi"] = ganzhi["yuezhi"]
        bengua["rizhi"] = ganzhi["rizhi"]
        biangua["yuezhi"] = ganzhi["yuezhi"]
        biangua["rizhi"] = ganzhi["rizhi"]
        return



