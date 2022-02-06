from django.contrib import admin
from .models import *

@admin.register(Questions)
class QuestionsAdmin(admin.ModelAdmin):
    list_display = ["id"]

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ["id"]

@admin.register(Form)
class FormAdmin(admin.ModelAdmin):
    list_display = ["id"]

@admin.register(Responses)
class ResponsesAdmin(admin.ModelAdmin):
    list_display = ["id"]


