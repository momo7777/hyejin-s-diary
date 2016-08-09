from django.contrib import admin
from models import diary_contents

# Register your models here.
class diary_contentsAdmin(admin.ModelAdmin):
    field = ('created_time', 'last_modified_time', 'image', 'preparing_person', 'title')

admin.site.register(diary_contents, diary_contentsAdmin)

