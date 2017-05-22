# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.generics import RetrieveAPIView
from .const import LiuYaoData
from .models import Liushisigua
from .models import Dizhi
from .models import Wuxing
from .models import Liuqin
from .models import Liushen
from .models import Huntianjiazi
from .serializer import LiushisiguaSerializer
from.boxcalender import BoxCalender

dizhi_name_set = ['liuyao_dizhi', 'wuyao_dizhi', 'siyao_dizhi', 'sanyao_dizhi', 'eryao_dizhi',
                  'chuyao_dizhi']
wuxing_name_set = ['liuyao_wuxing', 'wuyao_wuxing', 'siyao_wuxing', 'sanyao_wuxing', 'eryao_wuxing',
                   'chuyao_wuxing']
liuqin_name_set = ['liuyao_liuqin', 'wuyao_liuqin', 'siyao_liuqin', 'sanyao_liuqin', 'eryao_liuqin',
                   'chuyao_liuqin']
liushen_name_set = ['liuyao_liushen', 'wuyao_liushen', 'siyao_liushen', 'sanyao_liushen', 'eryao_liushen',
                   'chuyao_liushen']

dizhi_fushen_name_set = ['liuyao_fushen_dizhi', 'wuyao_fushen_dizhi', 'siyao_fushen_dizhi', 'sanyao_fushen_dizhi', 'eryao_fushen_dizhi',
                  'chuyao_fushen_dizhi']
wuxing_fushen_name_set = ['liuyao_fushen_wuxing', 'wuyao_fushen_wuxing', 'siyao_fushen_wuxing', 'sanyao_fushen_wuxing', 'eryao_fushen_wuxing',
                   'chuyao_fushen_wuxing']
liuqin_fushen_name_set = ['liuyao_fushen_liuqin', 'wuyao_fushen_liuqin', 'siyao_fushen_liuqin', 'sanyao_fushen_liuqin', 'eryao_fushen_liuqin',
                   'chuyao_fushen_liuqin']

dizhi_feishen_name_set = ['liuyao_feishen_dizhi', 'wuyao_feishen_dizhi', 'siyao_feishen_dizhi', 'sanyao_feishen_dizhi', 'eryao_feishen_dizhi',
                  'chuyao_feishen_dizhi']
wuxing_feishen_name_set = ['liuyao_feishen_wuxing', 'wuyao_feishen_wuxing', 'siyao_feishen_wuxing', 'sanyao_feishen_wuxing', 'eryao_feishen_wuxing',
                   'chuyao_feishen_wuxing']
liuqin_feishen_name_set = ['liuyao_feishen_liuqin', 'wuyao_feishen_liuqin', 'siyao_feishen_liuqin', 'sanyao_feishen_liuqin', 'eryao_feishen_liuqin',
                   'chuyao_feishen_liuqin']

yao_name_set = [
                {'label': '六爻', 'name': 'liuyao', 'time': 6},
                {'label': '五爻', 'name': 'wuyao', 'time': 5},
                {'label': '四爻', 'name': 'siyao', 'time': 4},
                {'label': '三爻', 'name': 'sanyao', 'time': 3},
                {'label': '二爻', 'name': 'eryao', 'time': 2},
                {'label': '初爻', 'name': 'chuyao', 'time': 1}
            ]

gender_mapper = {
    'male': '男',
    'female': '女'
}

matter_mapper = {
    'shiye': '事业',
    'hunyin': '婚姻',
    'caiwu': '财物',
    'kaoshi': '考试',
    'xunren': '寻人',
    'xunwu': '寻物',
    'jiankang': '健康'
}

# Create your views here.
class PaipanInput(APIView):
    def get(self, request):
        yao = {
            'nameSet': yao_name_set,
            'input_display': 'display:block;',
            'result_display': 'display:none;'
        }
        return Response(yao)

    def post(self, request):
        gua_image = self.get_gua_image(request)
        gua_detail = self.get_gua(request, gua_image)
        yao_detail = self.get_gua_detail_view(gua_detail)
        paipan_result = {
            'bengua': gua_detail['bengua'],
            'biangua': gua_detail['biangua'],
            'input_display': 'display:none;',
            'result_display': 'display:block;',
            'detail': yao_detail
        }
        return Response(paipan_result)

    def get_gua_image(self, request):
        yao_positions_for_nei_gua = ['sanyao', 'eryao', 'chuyao']
        yao_positions_for_wai_gua = ['liuyao', 'wuyao', 'siyao']
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
            for yao in LiuYaoData.yao:
                print("asdasd")
                print(yao)
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

        bengua_neigua = LiuYaoData.bagua.objects.filter(guaxiang=bengua_neigua_image).first()
        bengua_waigua = LiuYaoData.bagua.objects.filter(guaxiang=bengua_waigua_image).first()
        biangua_neigua = LiuYaoData.bagua.objects.filter(guaxiang=biangua_neigua_image).first()
        biangua_waigua = LiuYaoData.bagua.objects.filter(guaxiang=biangua_waigua_image).first()

        # 获得六十四卦的本卦信息
        bengua = LiushisiguaSerializer(Liushisigua.objects.filter(neigua=bengua_neigua.gua)
                                       .filter(waigua=bengua_waigua.gua).
                                       first()).data
        # 获得六十四卦的变卦信息
        biangua = LiushisiguaSerializer(Liushisigua.objects.filter(neigua=biangua_neigua.gua)
                                        .filter(waigua=biangua_waigua.gua)
                                        .first()).data
        # 附上卦的卦形信息
        bengua['guaxiang'] = bengua_waigua_image + bengua_neigua_image
        biangua['guaxiang'] = biangua_waigua_image + biangua_neigua_image

        # 获得卦属于的宫
        gong = bengua['gong']

        # 获得六十四卦的首宫卦信息
        shougonggua = LiushisiguaSerializer(Liushisigua.objects.filter(neigua=gong)
                                        .filter(waigua=gong)
                                        .first()).data

        # 获得卦的宫位五行
        wuxing = LiuYaoData.bagua.objects.filter(gua=gong).first().wuxing

        # 获得五行六亲的mapper
        wuxing_set = Wuxing.objects.filter(wuxing=wuxing).first()
        liuqin_set = Liuqin.objects.filter(liuqin=u"兄弟").first()
        wuxing_liuqin_mapper = {
            wuxing_set.wuxing: liuqin_set.liuqin,
            wuxing_set.sheng: liuqin_set.sheng,
            wuxing_set.ke: liuqin_set.ke,
            wuxing_set.beisheng: liuqin_set.beisheng,
            wuxing_set.beike: liuqin_set.beike
        }

        self.put_wuxing_liuqin_dizhi(bengua, bengua_neigua.gua, bengua_waigua.gua, wuxing, wuxing_liuqin_mapper)
        self.put_wuxing_liuqin_dizhi(biangua, biangua_neigua.gua, biangua_waigua.gua, wuxing, wuxing_liuqin_mapper)
        self.put_wuxing_liuqin_dizhi(shougonggua, gong, gong, wuxing, wuxing_liuqin_mapper)

        self.put_month_day(request, bengua)

        self.put_liushen(bengua)

        self.put_fushen_feishen(bengua, shougonggua)

        self.put_other_info(bengua, request)

        return {
            'bengua': bengua,
            'biangua': biangua,
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

    def put_fushen_feishen(self, bengua, shougonggua):
        bengua_liuqin_set = []
        for key in liuqin_name_set:
            bengua_liuqin_set.append(bengua[key])

        for i in range(0,6):
            if shougonggua[liuqin_name_set[i]] not in bengua_liuqin_set:
                bengua[liuqin_fushen_name_set[i]] = shougonggua[liuqin_name_set[i]]
                bengua[wuxing_fushen_name_set[i]] = shougonggua[wuxing_name_set[i]]
                bengua[dizhi_fushen_name_set[i]] = shougonggua[dizhi_name_set[i]]
                bengua[liuqin_feishen_name_set[i]] = bengua[liuqin_name_set[i]]
                bengua[wuxing_feishen_name_set[i]] = bengua[wuxing_name_set[i]]
                bengua[dizhi_feishen_name_set[i]] = bengua[dizhi_name_set[i]]

        return

    def put_other_info(self, bengua, request):
        gender = request.data['gender']
        matter = request.data['matter']
        bengua['gender'] = gender_mapper[gender]
        bengua['matter'] = matter_mapper[matter]
        return

    def get_gua_detail_view(self, gua):
        self.put_gua_chong_he_you_gui(gua['bengua'])
        self.put_gua_chong_he_you_gui(gua['biangua'])
        detail_view_set = [{},{},{},{},{},{}]
        for i in range(0, 6):
            print(detail_view_set[i])
            detail_view_set[i]['liushen'] = gua['bengua'][liushen_name_set[i]]
            detail_view_set[i]['yao'] = gua['bengua'][liuqin_name_set[i]] + gua['bengua'][dizhi_name_set[i]] + \
                                        gua['bengua'][
                                            wuxing_name_set[i]]
            detail_view_set[i]['yao_xiang'] = self.get_yao_xiang(gua['bengua'], yao_name_set[i]['time'])
            detail_view_set[i]['bian_yao'] = gua['biangua'][liuqin_name_set[i]] + gua['biangua'][dizhi_name_set[i]] + \
                                             gua['biangua'][
                                                 wuxing_name_set[i]]
            detail_view_set[i]['bian_yao_xiang'] = self.get_yao_xiang(gua['biangua'], yao_name_set[i]['time'])
            self.put_dong_mark(gua['bengua'], gua['biangua'], yao_name_set[i]['time'], detail_view_set, i)

            if liuqin_fushen_name_set[i] in gua['bengua']:
                detail_view_set[i]['fushen'] = gua['bengua'][liuqin_fushen_name_set[i]] + gua['bengua'][
                    dizhi_fushen_name_set[i]] + gua['bengua'][wuxing_fushen_name_set[i]]
            else:
                detail_view_set[i]['fushen'] = ''

        return detail_view_set

    def get_yao_xiang(self, gua, yao_position_number):
        image = gua['guaxiang']
        if image[yao_position_number-1] == '0':
            yao_image = '▅▅▅▅▅'
        else:
            yao_image = '▅▅　▅▅'

        if gua['shi'] == yao_position_number:
            yao_image += ' (世)'
        elif gua['ying'] == yao_position_number:
            yao_image += ' (应)'

        return yao_image

    def put_gua_chong_he_you_gui(self, gua):
        if gua['liuhe']:
            gua['gua'] += ' (六合)'
        elif gua['liuchong']:
            gua['gua'] += ' (六冲)'
        elif gua['youhun']:
            gua['gua'] += ' (游魂)'
        elif gua['guihun']:
            gua['gua'] += ' (归魂)'

    def put_dong_mark(self, bengua, biangua, yao_position_number, detail_view_set, i):
        if bengua['guaxiang'][yao_position_number-1] != biangua['guaxiang'][yao_position_number-1]:
            if bengua['guaxiang'][yao_position_number-1] == '0':
                detail_view_set[i]['yao_xiang'] += " X -->"
            else:
                detail_view_set[i]['yao_xiang'] += " O -->"



