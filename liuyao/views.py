# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.generics import RetrieveAPIView
from .const import LiuYaoData
from .boxcalender import BoxCalender


# Create your views here.
class PaipanInput(APIView):
    def get(self, request):
        yao = {
            'nameSet': LiuYaoData.yao_name_set,
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
            'neigua': nei_gua_image,
            'waigua': wai_gua_image
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

        bengua_neigua = self.filter_json_by_key('guaxiang', bengua_neigua_image, LiuYaoData.bagua)
        bengua_waigua = self.filter_json_by_key('guaxiang', bengua_waigua_image, LiuYaoData.bagua)
        biangua_neigua = self.filter_json_by_key('guaxiang', biangua_neigua_image, LiuYaoData.bagua)
        biangua_waigua = self.filter_json_by_key('guaxiang', biangua_neigua_image, LiuYaoData.bagua)

        # 获得六十四卦的本卦信息
        bengua = self.filter_json_by_key('neigua', bengua_neigua['gua'],
                                         self.filter_json_array_by_key('waigua', bengua_waigua['gua'],
                                                                       LiuYaoData.liushisigua))

        # 获得六十四卦的变卦信息
        biangua = self.filter_json_by_key('neigua', biangua_neigua['gua'],
                                          self.filter_json_array_by_key('waigua', biangua_waigua['gua'],
                                                                        LiuYaoData.liushisigua))
        # 附上卦的卦形信息
        bengua['guaxiang'] = bengua_waigua_image + bengua_neigua_image
        biangua['guaxiang'] = biangua_waigua_image + biangua_neigua_image

        # 获得卦属于的宫
        gong = bengua['gong']

        # 获得六十四卦的首宫卦信息
        shougonggua = self.filter_json_by_key('neigua', gong,
                                              self.filter_json_array_by_key('waigua', gong,
                                                                            LiuYaoData.liushisigua))

        # 获得卦的宫位五行
        wuxing = self.filter_json_by_key('gua', gong, LiuYaoData.bagua)['wuxing']

        # 获得五行六亲的mapper
        wuxing_set = self.filter_json_by_key('wuxing', wuxing, LiuYaoData.wuxing)
        liuqin_set = self.filter_json_by_key('liuqin', '兄弟', LiuYaoData.liuqin)
        wuxing_liuqin_mapper = {
            wuxing_set['wuxing']: liuqin_set['liuqin'],
            wuxing_set['sheng']: liuqin_set['sheng'],
            wuxing_set['ke']: liuqin_set['ke'],
            wuxing_set['beisheng']: liuqin_set['beisheng'],
            wuxing_set['beike']: liuqin_set['beike']
        }

        self.put_wuxing_liuqin_dizhi(bengua, bengua_neigua['gua'], bengua_waigua['gua'], wuxing, wuxing_liuqin_mapper)
        self.put_wuxing_liuqin_dizhi(biangua, biangua_neigua['gua'], biangua_waigua['gua'], wuxing,
                                     wuxing_liuqin_mapper)
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



        gua_neigua_dizhi = self.filter_json_by_key('neiwai', '内', self.filter_json_array_by_key('gua', gua_neigua,
                                                                                                LiuYaoData.huntianjiazi))
        gua_waigua_dizhi = self.filter_json_by_key('neiwai', '外', self.filter_json_array_by_key('gua', gua_waigua,
                                                                                                LiuYaoData.huntianjiazi))

        gua['liuyao_dizhi'] = gua_waigua_dizhi['san']
        gua['wuyao_dizhi'] = gua_waigua_dizhi['er']
        gua['siyao_dizhi'] = gua_waigua_dizhi['chu']
        gua['sanyao_dizhi'] = gua_neigua_dizhi['san']
        gua['eryao_dizhi'] = gua_neigua_dizhi['er']
        gua['chuyao_dizhi'] = gua_neigua_dizhi['chu']

        # 获得卦的各爻五行六亲
        for i in range(0, 6):
            gua[LiuYaoData.wuxing_name_set[i]] = self.filter_json_by_key('dizhi', gua[LiuYaoData.dizhi_name_set[i]], LiuYaoData.dizhi)[
                'wuxing']
            gua[LiuYaoData.liuqin_name_set[i]] = wuxing_liuqin_mapper[gua[LiuYaoData.wuxing_name_set[i]]]

        return

    def put_month_day(self, request, bengua):
        date = request.data['date']
        year = date[0:4]
        month = date[5:7]
        day = date[8:10]
        ganzhi = BoxCalender().day(int(year), int(month), int(day))
        bengua['yuezhi'] = ganzhi['yuezhi']
        bengua['rizhi'] = ganzhi['rizhi']
        bengua['rigan'] = ganzhi['rigan']
        return

    def put_liushen(self, gua):
        liushen_set = self.filter_json_by_key('rigan', gua['rigan'], LiuYaoData.liushen)
        gua['liuyao_liushen'] = liushen_set['liuyao']
        gua['wuyao_liushen'] = liushen_set['wuyao']
        gua['siyao_liushen'] = liushen_set['siyao']
        gua['sanyao_liushen'] = liushen_set['sanyao']
        gua['eryao_liushen'] = liushen_set['eryao']
        gua['chuyao_liushen'] = liushen_set['chuyao']
        return

    def put_fushen_feishen(self, bengua, shougonggua):
        bengua_liuqin_set = []
        for key in LiuYaoData.liuqin_name_set:
            bengua_liuqin_set.append(bengua[key])

        for i in range(0, 6):
            if shougonggua[LiuYaoData.liuqin_name_set[i]] not in bengua_liuqin_set:
                bengua[LiuYaoData.liuqin_fushen_name_set[i]] = shougonggua[LiuYaoData.liuqin_name_set[i]]
                bengua[LiuYaoData.wuxing_fushen_name_set[i]] = shougonggua[LiuYaoData.wuxing_name_set[i]]
                bengua[LiuYaoData.dizhi_fushen_name_set[i]] = shougonggua[LiuYaoData.dizhi_name_set[i]]
                bengua[LiuYaoData.liuqin_feishen_name_set[i]] = bengua[LiuYaoData.liuqin_name_set[i]]
                bengua[LiuYaoData.wuxing_feishen_name_set[i]] = bengua[LiuYaoData.wuxing_name_set[i]]
                bengua[LiuYaoData.dizhi_feishen_name_set[i]] = bengua[LiuYaoData.dizhi_name_set[i]]

        return

    def put_other_info(self, bengua, request):
        gender = request.data['gender']
        matter = request.data['matter']
        bengua['gender'] = LiuYaoData.gender_mapper[gender]
        bengua['matter'] = LiuYaoData.matter_mapper[matter]
        return

    def get_gua_detail_view(self, gua):
        self.put_gua_chong_he_you_gui(gua['bengua'])
        self.put_gua_chong_he_you_gui(gua['biangua'])
        detail_view_set = [{}, {}, {}, {}, {}, {}]
        for i in range(0, 6):
            print(detail_view_set[i])
            detail_view_set[i]['liushen'] = gua['bengua'][LiuYaoData.liushen_name_set[i]]
            detail_view_set[i]['yao'] = gua['bengua'][LiuYaoData.liuqin_name_set[i]] + gua['bengua'][LiuYaoData.dizhi_name_set[i]] + \
                                        gua['bengua'][
                                            LiuYaoData.wuxing_name_set[i]]
            detail_view_set[i]['yao_xiang'] = self.get_yao_xiang(gua['bengua'], LiuYaoData.yao_name_set[i]['time'])
            detail_view_set[i]['bian_yao'] = gua['biangua'][LiuYaoData.liuqin_name_set[i]] + gua['biangua'][LiuYaoData.dizhi_name_set[i]] + \
                                             gua['biangua'][
                                                 LiuYaoData.wuxing_name_set[i]]
            detail_view_set[i]['bian_yao_xiang'] = self.get_yao_xiang(gua['biangua'], LiuYaoData.yao_name_set[i]['time'])
            self.put_dong_mark(gua['bengua'], gua['biangua'], LiuYaoData.yao_name_set[i]['time'], detail_view_set, i)

            if LiuYaoData.liuqin_fushen_name_set[i] in gua['bengua']:
                detail_view_set[i]['fushen'] = gua['bengua'][LiuYaoData.liuqin_fushen_name_set[i]] + gua['bengua'][
                    LiuYaoData.dizhi_fushen_name_set[i]] + gua['bengua'][LiuYaoData.wuxing_fushen_name_set[i]]
            else:
                detail_view_set[i]['fushen'] = ''

        return detail_view_set

    def get_yao_xiang(self, gua, yao_position_number):
        image = gua['guaxiang']
        if image[yao_position_number - 1] == '0':
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
        if bengua['guaxiang'][yao_position_number - 1] != biangua['guaxiang'][yao_position_number - 1]:
            if bengua['guaxiang'][yao_position_number - 1] == '0':
                detail_view_set[i]['yao_xiang'] += " X -->"
            else:
                detail_view_set[i]['yao_xiang'] += " O -->"

    def filter_json_by_key(self, key, value, array):
        for data in array:
            if key in data:
                if data[key] == value:
                    return data
            else:
                return None

        return None

    def filter_json_array_by_key(self, key, value, array):
        filtered_array = []
        for data in array:
            if key in data:
                if data[key] == value:
                    filtered_array.append(data)

        return filtered_array
