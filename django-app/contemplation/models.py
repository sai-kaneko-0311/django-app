from django.db import models


class Member(models.Model):
    id = models.IntegerField('id', primary_key=True)
    name = models.CharField('name', max_length=255)


class Comment(models.Model):
    id = models.IntegerField('id', primary_key=True)
    text = models.TextField('text')
    commented_at = models.DateField('commented_at')


class Room(models.Model):
    id = models.CharField('id', primary_key=True, max_length=64)
    created_by = models.IntegerField('created_by')
