from django.contrib import admin
from .models import TeamName, CsvUpload

# Register your models here.

admin.site.register(CsvUpload)
admin.site.register(TeamName)