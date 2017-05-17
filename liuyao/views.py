# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Bagua
from .models import Liushisigua
from .models import Dizhi
from .models import Wuxing
from .models import Liuqin
from .models import Huntianjiazi

# Create your views here.
def index(request):
    url = 'liuyao/index.html'
    bagua = get_object_or_404(Bagua, pk="乾")
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