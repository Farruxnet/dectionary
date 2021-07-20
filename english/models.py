from django.db import models

class EnglishWord(models.Model):
    LEVEL = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
    )
    uz  = models.CharField(blank=True, max_length=100, verbose_name='O\'zbek')
    en  = models.CharField(blank=True, max_length=100, verbose_name='Ingliz')
    level = models.CharField(choices=LEVEL, blank=True, max_length=100)
