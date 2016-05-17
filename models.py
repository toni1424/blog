from django.contrib.auth.models import User
from django.db import models
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from django.views.generic.list import ListView

SHORT_TEXT_LEN = 600


class Article(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    user = models.ForeignKey(User)
    datetime = models.DateTimeField(u'Дата публикации')

    def __str__(self):
        return self.title

    def get_short_text(self):
        if len(self.text) > SHORT_TEXT_LEN:
            return self.text[:SHORT_TEXT_LEN]
        else:
            return self.text
