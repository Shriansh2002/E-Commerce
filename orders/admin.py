from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    fields = ('product', 'price', 'quantity', 'created')
    readonly_fields = ('product', 'price', 'quantity', 'created')
    #raw_id_fields = ['product']



class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','user','paid','created','updated']

    list_filter = ['paid','created','updated']
    inlines = [OrderItemInline]
    readonly_fields = ['user']
    search_fields = ('email',)

admin.site.register(Order, OrderAdmin)
