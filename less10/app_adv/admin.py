from django.contrib import admin
from .models import Advert
from django.utils.html import format_html
# Register your models here.

class AdvertAdmin(admin.ModelAdmin):
    list_display = ["id","title","user","price","auction","created_date","update_date","img"]
    list_filter = ["auction","created_at"]
    actions = ["auctionChangeTrue","auctionChangeFalse"]

    @admin.action(description="Добавить торг")
    def auctionChangeTrue(self,request,queryset):
         return queryset.update(auction=True)

    @admin.action(description="Убрать торг")
    def auctionChangeFalse(self, request, queryset):
        return queryset.update(auction=False)
    @admin.display()
    def img(self,obj):
        if obj.image:
            return format_html('<img src="{}" width="80">'.format(obj.image.url))
        else:
            return format_html('<img src="{}" width="80">'.format("/static/img/pic.png"))

    fieldsets = (
        ("Общее",{"fields":("title","descript","image")}),
        ("Финансы", {"fields": ("price", "auction"),"classes":["collapse"]}),
    )

admin.site.register(Advert, AdvertAdmin)