from django.db import models
from django.utils.translation import gettext_lazy as _
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from django.utils import timezone

from django.utils.text import slugify

# Create your models here.
class Product(models.Model):
    flag_type=[
        ('New','New'),
        ('Sale','Sale'),
        ('Feature','Feature')

    ]
    
    name=models.CharField(max_length=120,verbose_name=_('name_product'))
    flag=models.CharField(_('flag'),max_length=50,choices=flag_type)
    price=models.DecimalField('price',max_digits=6, decimal_places=2)
    image=models.ImageField(upload_to='photo_product',verbose_name=_('image'))
    sku=models.IntegerField(_('sku'),unique=True )
    subtitle=models.TextField(_('subtitle'),max_length=5000)
    description=models.TextField(_('descriptions'),max_length=50000)
    slug=models.SlugField(null=True,blank=True,verbose_name=_('slug'))
    tags = TaggableManager()
    brand=models.ForeignKey('Brand',on_delete=models.SET_NULL,null=True)


    def __str__(self):
        return self.name
    def save(self,*args,**kwargs):
        self.slug=self.name
        super(Product,self).save(*args,**kwargs)

class Brand(models.Model):
    name=models.CharField(max_length=120)
    image=models.ImageField(upload_to='photo_brand')
    slug=models.SlugField(null=True,blank=True)

    def __str__(self):
        return self.name
    def save(self,*args,**kwargs):
        self.slug=self.name
        super(Brand,self).save(*args,**kwargs)

class ProductImage(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='productimage_product')
    image=models.ImageField(upload_to='images')

    def __str__(self):
        return str(self.product)
class Review(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name='review_user')
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='review_product')
    review=models.TextField(max_length=1000)
    rate=models.CharField(_("rate"), max_length=50,choices=[(i,i) for i in range(1,6)])
    publish_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user}-{self.product}-{self.rate}'

    





    


