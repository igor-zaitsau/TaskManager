from django.contrib import admin
from .models import *

#login: admin
#password: admin

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'time_create', 'done')
    list_display_links = ('title',)
    search_fields = ('title',  'task')
    list_editable = ('done',)
    list_filter = ('time_create', 'done')

admin.site.register(Task, TaskAdmin)

