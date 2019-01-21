from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    date_created = models.DateTimeField('date published')
    date_updated = models.DateTimeField('date published', null=True, blank=True)
    content = models.TextField(null=True)



    def __str__(self):
        return 'post: {}'.format(self.title)


class Comment(models.Model):

    date_created = models.DateTimeField('date published')

    content = models.TextField(null=True)
