from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True,db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

   # class Meta:
        #ordering = ('name')
        #verbose_name = 'category'
        #verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('produits:product_list_by_category',args=[self.slug])

class Product(models.Model):
    Category = models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE)
    nameProd = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=150, db_index=True)
    description = models.TextField(blank=True)
    price = models.FloatField(default=None)
    #price = models.DecimalField(max_digits=10, decimal_places=3)
    available = models.BooleanField(default=True)
    stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/%Y%m%d', blank=True)

   #class Meta:
       # ordering = ('nameProd', ),
        #indexes = (('id','slug'),)

    def __str__(self):
        return self.nameProd
    def get_absolute_url(self):
        return reverse('produits:product_detail',args=[self.pk,self.slug])