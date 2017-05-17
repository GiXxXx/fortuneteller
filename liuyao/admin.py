# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Bagua
from .models import Liushisigua
from .models import Dizhi
from .models import Wuxing
from .models import Liuqin
from .models import Huntianjiazi
# Register your models here.

admin.site.register(Bagua)
admin.site.register(Liushisigua)
admin.site.register(Dizhi)
admin.site.register(Wuxing)
admin.site.register(Liuqin)
admin.site.register(Huntianjiazi)