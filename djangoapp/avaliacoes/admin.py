from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Feedback

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'data_hora')
    list_filter = ('tipo', 'data_hora')
