from django.contrib import admin
from .models import Tag
# Register your models here.
class TagAdmin(admin.ModelAdmin): 
    list_display = ('name', 'description_bref', 'create') 
    search_fields = ["name"] 
    ordering = ["-create"]
    prepopulated_fields={'slug':('name',)}
    fields=('name','slug','image','description')
admin.site.register(Tag, TagAdmin)
