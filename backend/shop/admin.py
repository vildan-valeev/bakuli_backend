from django.contrib import admin
from shop.models import Category, Item, CartItem, Cart, Order, Store, Actual, Ingredient, IngredientCategory


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', ]
    list_display_links = ['id', ]
    list_editable = ['name', ]


class IngredientAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'is_replaceable']
    list_display_links = ['id', ]
    list_editable = ['title', 'is_replaceable', 'category']


class ItemAdmin(admin.ModelAdmin):
    filter_horizontal = ['ingredients']
    list_filter = ['category', 'additional', 'store']
    list_display = ['id', 'title', 'get_categories', 'price', 'additional', 'created', 'published']
    list_display_links = ['id', 'title', ]
    list_editable = ['published', 'additional']
    readonly_fields = ['created', 'updated']


class CartItemAdmin(admin.ModelAdmin):
    list_display = ['id', '__str__', 'parent', 'customer', 'cart', 'qty_item', 'total_price', 'created', 'updated']
    list_display_links = ['id', '__str__', ]
    readonly_fields = ['created', 'updated']


class CartAdmin(admin.ModelAdmin):
    list_display = ['id', 'final_price', 'created', 'updated']
    list_display_links = ['id', ]
    readonly_fields = ['created', 'updated']


class ActualAdmin(admin.ModelAdmin):
    list_display_links = ['id', 'title', ]
    list_display = ['id', 'title', 'published', 'created', 'updated']
    readonly_fields = ['created', 'updated']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', '__str__', 'status', 'created', 'updated']
    list_display_links = ['id', '__str__', ]
    readonly_fields = ['created', 'updated']
    list_filter = ['store', 'status', ]


class StoreAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'city', 'street', 'house_number', 'index']
    # list_editable = ['title', 'city', 'street', 'house_number', 'index']
    list_display_links = ['id', 'title']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(CartItem, CartItemAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Actual, ActualAdmin)

admin.site.register(IngredientCategory)