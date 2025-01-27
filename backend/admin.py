from django.contrib import admin
from .models import Category

# #register your models here.
# admin.site.register(Category)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','id')
    #search field
    search_fields = ('name',)
admin.site.register(Category,CategoryAdmin)
