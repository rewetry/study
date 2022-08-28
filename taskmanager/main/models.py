from django.db import models


class Task(models.Model):
    title = models.CharField('назва відсутня',max_length=50)
    task = models.TextField('опис')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name ='завдвня'
        verbose_name_plural ='завдвня'
