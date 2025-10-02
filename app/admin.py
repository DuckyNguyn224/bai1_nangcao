from django.contrib import admin
from .models import Banner, Product, ContentSection

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'active')
    list_filter = ('active',)
    search_fields = ('title', 'subtitle')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'active', 'featured', 'flash_deals', 'last_minute')
    list_filter = ('active', 'featured', 'flash_deals', 'last_minute')
    search_fields = ('title',)

@admin.register(ContentSection)
class ContentSectionAdmin(admin.ModelAdmin):
    list_display = ('page', 'section_name')
    search_fields = ('page', 'section_name')

# Register your models here.
