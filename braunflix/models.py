from django.db import models

class Program(models.Model):
    KIND = (('F', 'Film'),('T', 'TV show'),)

    title = models.CharField(max_length=50)
    kind = models.CharField(max_length=1,choices=KIND, blank=False, null=False,default='F')
    release_date = models.DateField()
    likes = models.PositiveIntegerField(default=0)
    dislikes= models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
    