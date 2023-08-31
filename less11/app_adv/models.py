from django.db import models
from django.utils import timezone
from django.utils.html import format_html
from django.contrib.auth import get_user_model

User=get_user_model()
class Advert(models.Model):
    title=models.CharField("Название",max_length=128)
    descript=models.TextField("Описание")
    price=models.DecimalField("Цена",max_digits=10,decimal_places=2)
    auction=models.BooleanField("Торг",help_text="Нажмите, если торг уместен")
    created_at=models.DateTimeField(auto_now_add=True)
    update_ap=models.DateTimeField(auto_now=True)
    user=models.ForeignKey(User,verbose_name="Пользователь",on_delete=models.CASCADE,null=True)
    image=models.ImageField("Изображение",upload_to='images/')
    def __str__(self):
        return "%s (%s)" % (self.__class__.__name__, "id="+str(self.id)+", title="+self.title+", price="+str(self.price))
    def created_date(self):
        if self.created_at.date()==timezone.now().date():
            created_time=self.created_at.time().strftime("%H:%M")
            return format_html('<span style="color: green; font-weight: bold;"> Сегодня в {}</span>',created_time)
        return self.created_at.strftime("%d.%m.%Y в %H:%M")
    def update_date(self):
        if self.update_ap.date()==timezone.now().date():
            created_time=self.update_ap.time().strftime("%H:%M")
            return format_html('<span style="color: red; font-weight: bold;"> Сегодня в {}</span>',created_time)
        return self.update_ap.strftime("%d.%m.%Y в %H:%M")
    class Meta:
        db_table = "advertisements"