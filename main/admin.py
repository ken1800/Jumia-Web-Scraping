from django.contrib import admin
from main.models import Quote,Jumia,Perfecto

class QuoteAdmin(admin.ModelAdmin):
    list_display = ('author', 'text', )
class JumiaAdmin(admin.ModelAdmin):
    list_display = ('name','discount','price')
# Register your models here.
admin.site.register(Quote, QuoteAdmin)
admin.site.register(Jumia)
admin.site.register(Perfecto)