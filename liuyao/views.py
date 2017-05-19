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
# Create your views here.
def index(request):
    url = 'liuyao/index.html'
    bagua = Bagua.objects.all()
    context = {
        'bagua': bagua,
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
        guaImage = self.getGuaImage(request)
        return Response(gua)

    def getGuaImage(self, request):
        yaoSet = Yao.objects.all()
        yaoSerializer = YaoSerializer(yaoSet, many=True)
        coinSet = request.data
        benGua = ""
        bianGua = ""
        yaoPositions = ['chuyao', 'eryao', 'sanyao', 'siyao', 'wuyao', 'liuyao']
        for position in yaoPositions:
            for yao in yaoSerializer.data:
                if yao['yao'] == coinSet[position]:
                    benGua += yao['image']
                    if yao['dong']:
                        bianGua += yao['reverse']
                    else:
                        bianGua += yao['image']

        return {
            'benGua': benGua,
            'bianGua': bianGua
        }

    def getGua(selfself, guaImage):
        benGua = Liushisigua.objects.raw("select * from liuyao_liushisigua where ")