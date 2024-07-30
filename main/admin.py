from django.contrib import admin
from .models import Goods, Question

class QuestionAdmin(admin.ModelAdmin):
    list_display = ["time_created", "question"]

admin.site.register(Goods)
admin.site.register(Question, QuestionAdmin)

