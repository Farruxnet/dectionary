from django.db import models

class Config(models.Model):
    start_text = models.TextField()

    class Meta:
        verbose_name = "Bot sozlamalari"
        verbose_name_plural = "Bot sozlamalari"
        
    def __str__(self):
        return self.start_text
