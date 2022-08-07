from django.contrib import admin
from .models import Order

class Orders(admin.ModelAdmin):
    list_display = ('id', 'cliente',)
    list_display_links = ('id', 'cliente',)
    search_fields = ('Order',)

admin.site.register(Order, Orders)