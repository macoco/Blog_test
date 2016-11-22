from django.db import models

# Create your models here.
class Article(models.Model):
    """docstring for Article"""
    title = models.CharField(max_length = 100) #博客标题
    category = models.CharField(max_length = 50, blank = True) #标签
    date_time = models.DateTimeField(auto_now_add = True) #博客日期
    content = models.TextField(blank = True, null = True) #正文


    def __unicode__(self):
        return self.title

    class Meta:
        """docstring for Meta"""
        ordering = ['-date_time']


