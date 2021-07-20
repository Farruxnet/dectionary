from django.db import models
from django.utils import timezone

class TgUser(models.Model):
    tg_id = models.IntegerField(verbose_name='Telegram ID')
    name = models.CharField(null=True, blank=True, max_length=200, verbose_name='Ismi')
    username = models.CharField(max_length=32, null=True, blank=True, verbose_name='Username')
    telefon = models.CharField(max_length=25, null=True, blank=True, verbose_name='Telefon raqam')
    create_at = models.DateTimeField(default=timezone.now, verbose_name='Qo\'shilgan vaqti')
    account = models.IntegerField(default=0, verbose_name='Hisob')
    step = models.IntegerField(default=0, verbose_name='---')
    class Meta:
        verbose_name = "TELEGRAM FOYDALANUVCHILAR"
        verbose_name_plural = "Telegram foydalanuvchilar"
    def __str__(self):
        return self.name
