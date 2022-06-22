from django.contrib import admin
from .models import Product,Comment

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity', 'price','sell', 'image','product_of_the_day','visible_in_shop')
    search_fields = ('name','price',)
    
class CommentAdmin(admin.ModelAdmin):
    list_display = ('product', 'author', 'created', 'updated', 'active')
    list_filter = ('product', 'author', 'active')
    search_fields = ('product__name','author__username','body',)

admin.site.register(Product,ProductAdmin)
admin.site.register(Comment,CommentAdmin)