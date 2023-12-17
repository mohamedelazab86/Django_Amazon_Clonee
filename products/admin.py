from django.contrib import admin
from .models import Product,Brand,ProductImage
from django_summernote.admin import SummernoteModelAdmin

class Productinline(admin.TabularInline):
    model=ProductImage

class ProductAdmin(SummernoteModelAdmin):
    list_display=['name']
    list_filter=['price']
    search_fields=['name']
    summernote_fields = ('subtitle','description')
    inlines=[Productinline,]
    
# Register your models here.
admin.site.register(Product,ProductAdmin)
admin.site.register(Brand)
#admin.site.register(ProductImage)
