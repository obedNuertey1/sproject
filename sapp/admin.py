from django.contrib import admin
from .models import SModel

# Register your models here.


class SModelAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name',
                    'isComplete', 'date', 'pdf_file',)


admin.site.register(SModel, SModelAdmin)
