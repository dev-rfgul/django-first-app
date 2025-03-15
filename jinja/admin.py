from django.contrib import admin
from .models import ChaiVariety, chaiCertificates, chaiReview, store

# Register your models here.

class ChaiReviewInLine(admin.TabularInline):
    model=chaiReview
    extra=2
class chaiVarietyAdmin(admin.ModelAdmin):
    list_display=('name','type','date_added', 'price', 'description')
    inlines=[ChaiReviewInLine]
class chaiStoreAdmin(admin.ModelAdmin):
    list_display=('name', 'location', )
    filter_horizontal=('chai_varities',)

class chaiCertificatesAdmin(admin.ModelAdmin):
    list_display=('chai','issued_date')

# admin.site.register(ChaiVariety, )
# this will display the django default style but to inject our own classe we have to follow this syntax
admin.site.register(ChaiVariety,chaiVarietyAdmin)
admin.site.register(store,chaiStoreAdmin)
admin.site.register(chaiCertificates,chaiCertificatesAdmin)
# admin.site.register(chaiReview, )