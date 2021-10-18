from django.db import models



class Post(models.Model):

    categories = [
        ('technology' , 'technology'),
        ('science' , 'science'),
        ('education' , 'education'),
        ('business' , 'business'),
        ('entrepreneurship' , 'entrepreneurship'),
    ]

    title = models.CharField(max_length=100)
    brief = models.TextField(max_length=500)
    description = models.TextField(max_length=10000)
    image = models.ImageField(upload_to='blog_pics')
    category = models.CharField(max_length=100,null=True,blank=True,choices=categories,)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_posted',]