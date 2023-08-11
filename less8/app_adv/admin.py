from django.contrib import admin
from .models import Advert
# Register your models here.

class AdvertAdmin(admin.ModelAdmin):
    list_display = ["id","title","price","auction","created_date","update_date"]
    list_filter = ["auction","created_at"]
    actions = ["auctionChangeTrue","auctionChangeFalse"]

    @admin.action(description="Добавить торг")
    def auctionChangeTrue(self,request,queryset):
         return queryset.update(auction=True)

    @admin.action(description="Убрать торг")
    def auctionChangeFalse(self, request, queryset):
        return queryset.update(auction=False)

    fieldsets = (
        ("Общее",{"fields":("title","descript")}),
        ("Финансы", {"fields": ("price", "auction"),"classes":["collapse"]}),
    )

admin.site.register(Advert, AdvertAdmin)