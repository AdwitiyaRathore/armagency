from django.contrib import admin
from .models import StuffingSheetModel, TotalStuffingValue

# Register your models here.
admin.site.register(StuffingSheetModel)
admin.site.register(TotalStuffingValue)