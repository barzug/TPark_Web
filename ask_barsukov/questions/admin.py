# coding=utf-8
from django.contrib import admin

from questions.models import *

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Tag)