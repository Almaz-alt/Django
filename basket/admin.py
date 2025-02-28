from .models import ParsedData
from django.contrib import admin

@admin.register(ParsedData)
class ParsedDataAdmin(admin.ModelAdmin):
    list_display = ["title",]