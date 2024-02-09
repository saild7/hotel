from django.db import models
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models import Avg,Count


# Create your models here.
class Room(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )

    name = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    image=models.ImageField(upload_to='images/',null=False)
    price = models.DecimalField(max_digits=12, decimal_places=2,default=0)
    size=models.DecimalField(max_digits=5,decimal_places=2)
    max_adult=models.IntegerField(default=0)
    max_children=models.IntegerField(default=0)
    detail=RichTextUploadingField()
    significant_feature = RichTextUploadingField()
    slug = models.SlugField(null=False, unique=True)
    status=models.CharField(max_length=10,choices=STATUS)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    ## method to create a fake table field in read only mode
    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    
    image_tag.short_description ='Image'

class Images(models.Model):
    product=models.ForeignKey(Room,on_delete=models.CASCADE)
    title = models.CharField(max_length=50,blank=True)
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.title



    