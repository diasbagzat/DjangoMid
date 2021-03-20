from django.db import models

class BookJournalBase (models.Model):
    name = models.CharField(max_length=255, null=True, verbose_name='Название')
    price = models.IntegerField(verbose_name='Цена')
    description = models.TextField(null=True, verbose_name='Описание')
    created_at = models.DateTimeField(verbose_name='Дата')

    class Meta:
        abstract = True


class Book(BookJournalBase):
    num_pages = models.IntegerField(verbose_name='Страницы')
    genre = models.CharField(max_length=255, null=True)

    class Meta:
        ordering = ['genre']

class Journal(BookJournalBase):
    type = models.TextField(max_length=255, null=True)
    publisher = models.TextField(max_length=255, null=True, verbose_name='Издатель')










