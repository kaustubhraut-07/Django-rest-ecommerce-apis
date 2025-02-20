from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from io import BytesIO
from django.core.files import File
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    

    class Meta:
        ordering=['name']

    def __str__(self):
        return self.name
    
    def get_abstulate_url(self):
        return f'/{self.slug}/'
    

class Products(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='uploads/')
    thumbnail=models.ImageField(upload_to='uploads/thumbnail/', null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        ordering=['-date_added']

    def __str__(self):
        return self.name
    
    def get_abstulate_url(self):
        return f'/{self.category.slug}/{self.slug}/'
    
    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''
    
    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail=self.make_thumbnail(self.image)
                self.save()
                return 'http://127.0.0.1:8000' + self.thumbnail.url
        return ''
    
    def make_thumbnail(self, image, size=(300, 200)):
        img=Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)
        thumb_io=BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)
        thumbnail=File(thumb_io, name=image.name)
        return thumbnail
