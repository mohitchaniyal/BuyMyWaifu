from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField() 
    is_nsfw = models.BooleanField(default=False)
    class Meta:
        ordering = ('name',)
    
    def __str__(self):
        return self.name

class Waifu(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    image_url = models.URLField(default='#')

    class Meta:
        ordering=("-created_at",) #negetive means decending order
    
    def __str__(self):
        return self.name
    

