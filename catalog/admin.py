
from django.contrib import admin
from .models import Producer, Type, Product, ProductPackage

class ProductPackageInline(admin.TabularInline):
    model = ProductPackage
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'producer', 'type', 'is_visible')
    list_filter = ('producer', 'type', 'is_visible')
    search_fields = ('name',)
    inlines = [ProductPackageInline]

    @admin.display(boolean=True)
    def is_visible(self, obj):
        return not obj.is_hidden

class ProducerAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_visible')
    search_fields = ('name',)

    @admin.display(boolean=True)
    def is_visible(self, obj):
        return not obj.is_hidden

class TypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Producer, ProducerAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Product, ProductAdmin)
