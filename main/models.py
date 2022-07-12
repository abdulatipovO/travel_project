from statistics import mode
from tabnanny import verbose
from django.db import models


# Create your models here.


class Direction(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField("Ma'lumot", blank=True)
    image = models.ImageField(upload_to='images')
    duration = models.PositiveIntegerField("Davomiyligi", default=10)
    price = models.PositiveIntegerField(default=100, verbose_name="UZS")
    price_usd = models.PositiveIntegerField(default=100, verbose_name="USD")
    leave = models.DateField("Ketish sanasi (To'ldirish shart emas)", blank=True,null=True)
    back_to = models.DateField("Qaytish sanasi (To'ldirish shart emas)", blank=True,null=True)


    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = "Yo'nalish"
        verbose_name_plural = "Yo'nalishlar"
    


class CategoryNews(models.Model):
    title = models.CharField(max_length=50, blank=True)
    reg_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = "Yangilik_Yo'nalishi"
        verbose_name_plural = "Yangiliklar_Yo'nalishlari"


class Contact(models.Model):
    name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True,null=True)
    subject = models.CharField(max_length=50,blank=True)
    text = models.TextField(max_length=255, blank=True)
    reg_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.name)





class News(models.Model):
    category = models.ForeignKey(CategoryNews,on_delete=models.PROTECT, null=True, related_name="news" )
    title = models.CharField(max_length=60, blank=True)
    text = models.TextField(blank=True)
    image = models.ImageField(upload_to='images', blank=True)
    views = models.PositiveIntegerField(default=0,blank=True)
    reg_date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.title)

    class Meta:
        verbose_name = "Yangilik"
        verbose_name_plural = "Yangiliklar"

class SubscribeNews(models.Model):
    name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    reg_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.name)