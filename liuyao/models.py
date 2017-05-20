# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Bagua(models.Model):
    gua = models.CharField(primary_key='true', max_length=250)
    fangwei = models.CharField(max_length=250)
    qinshu = models.CharField(max_length=250)
    yuzhou = models.CharField(max_length=250)
    yinyang = models.CharField(max_length=250)
    wuxing = models.CharField(max_length=250)
    guaxiang = models.CharField(max_length=250)

    def __str__(self):
        return self.gua

class Liushisigua(models.Model):
    xu =  models.IntegerField(primary_key='true')
    gua = models.CharField(max_length=250)
    gong = models.CharField(max_length=250)
    waigua = models.CharField(max_length=250)
    neigua = models.CharField(max_length=250)
    shi = models.IntegerField()
    ying = models.IntegerField()
    liuchong = models.BooleanField()
    liuhe = models.BooleanField()
    youhun = models.BooleanField()
    guihun = models.BooleanField()

    def __str__(self):
        return self.gua

class Huntianjiazi(models.Model):
    id = models.IntegerField(primary_key='true')
    gua = models.CharField(max_length=250)
    neiwai = models.CharField(max_length=250)
    chu = models.CharField(max_length=250)
    er = models.CharField(max_length=250)
    san = models.CharField(max_length=250)

    def __str__(self):
        return self.id

class Dizhi(models.Model):
    dizhi = models.CharField(primary_key='true', max_length=250)
    yinyang = models.CharField(max_length=250)
    wuxing = models.CharField(max_length=250)

    def __str__(self):
        return self.dizhi

class Wuxing(models.Model):
    wuxing = models.CharField(primary_key='true', max_length=250)
    sheng = models.CharField(max_length=250)
    ke = models.CharField(max_length=250)
    beisheng = models.CharField(max_length=250)
    beike = models.CharField(max_length=250)

    def __str__(self):
        return self.wuxing

class Liuqin(models.Model):
    liuqin = models.CharField(primary_key='true', max_length=250)
    sheng = models.CharField(max_length=250)
    ke = models.CharField(max_length=250)
    beisheng = models.CharField(max_length=250)
    beike = models.CharField(max_length=250)

    def __str__(self):
        return self.liuqin

class Yao(models.Model):
    yao = models.CharField(primary_key='true', max_length=250)
    coin = models.CharField(max_length=250)
    name = models.CharField(max_length=250)
    image = models.CharField(max_length=250)
    dong = models.BooleanField()
    reverse = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Liushen(models.Model):
    rigan = models.CharField(primary_key='true', max_length=250)
    liuyao = models.CharField(max_length=250)
    wuyao = models.CharField(max_length=250)
    siyao = models.CharField(max_length=250)
    sanyao = models.CharField(max_length=250)
    eryao = models.CharField(max_length=250)
    chuyao = models.CharField(max_length=250)

    def __str__(self):
        return self.name