from django.db import models
from accounts.models import CustomUser

class Product(models.Model):

    name = models.CharField(max_length=20,)
    price = models.CharField(max_length=10,)
    sell = models.CharField(max_length=10, default='')
    description = models.CharField(max_length=300,)
    image = models.ImageField(upload_to='images/')

    def get_absolute_url(self):
        return reverse('product',
                        args=[])
                              
    def __str__(self):
        return '='.join([self.name, self. price+' руб'])

class Comment(models.Model):
    product = models.ForeignKey(Product, related_name='comments',on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, related_name='user',on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ('created',)
    
    def __str__(self):
        return 'Comment by {} on {}'.format(self.author, self.product)