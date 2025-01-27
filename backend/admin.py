from django.contrib import admin
from .models import Category

# #register your models here.
# admin.site.register(Category)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','id')
    #search field
    search_fields = ('name',)
    #add filters for name field
    list_filter = ('name',)
admin.site.register(Category,CategoryAdmin)
