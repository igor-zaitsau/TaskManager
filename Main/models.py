from django.db import models
from django.urls import reverse


class Task(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    task = models.TextField(verbose_name='Задача')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время обновления')
    done = models.BooleanField(default=False, verbose_name='Статус')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/update/{self.pk}'  # reverse('updateTask', kwargs={'task_id': self.pk})

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'