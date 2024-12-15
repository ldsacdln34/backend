from django.contrib import admin
from .models import Url
from .models import BlackList
from .models import WhiteList
from .models import Graylist

admin.site.register(Url)
admin.site.register(BlackList)
admin.site.register(WhiteList)
admin.site.register(Graylist)
