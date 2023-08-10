from django.db import models

class Advert(models.Model):
    title=models.CharField("Название",max_length=128)
    descript=models.TextField("Описание")
    price=models.DecimalField("Цена",max_digits=10,decimal_places=2)
    auction=models.BooleanField("Торг",help_text="True, если торг уместен")
    created_at=models.DateTimeField(auto_now_add=True)
    update_ap=models.DateTimeField(auto_now=True)
    def __str__(self):
        return "%s (%s)" % (self.__class__.__name__, "id="+str(self.id)+", title="+self.title+", price="+str(self.price))

    class Meta:
        db_table = "advertisements"