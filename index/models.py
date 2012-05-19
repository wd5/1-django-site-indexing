from django.db import models

class Site(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField('URL', max_length=255)
    tags = models.TextField('Meta Tags')
    description = models.TextField()
    post_date = models.DateTimeField('Date Posted', auto_now_add=True)
    views = models.PositiveIntegerField(default=0)
    clicks = models.PositiveIntegerField(default=0)
    
    def __unicode__(self):
        return self.name

class Page(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField('URL Slug', max_length=100, unique=True)
    tags = models.TextField('Meta Tags')
    body = models.TextField()
    order = models.PositiveIntegerField(default=0, blank=False, null=False)
    
    def __unicode__(self):
        return self.name
