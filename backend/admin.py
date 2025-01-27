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
    #sorting by name in descending order
    ordering = ['-name'] # descending order use the negative sign
admin.site.register(Category,CategoryAdmin)
