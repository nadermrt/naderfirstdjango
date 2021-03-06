from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length = 100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    image = models.ImageField(default='default.jpg',blank=True)
    # add in arthor

    def __str__(self):
        return self.title
    
    def snippet(self):
        
        if len(self.body)<50:
            return self.body
        
        return self.body[0:50] + ' ...'