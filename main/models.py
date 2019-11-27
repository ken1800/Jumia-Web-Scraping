from django.db import models

class Quote(models.Model):
    """
    The scrapped data will be saved in this model
    """
    text = models.TextField()
    author = models.CharField(max_length=512)
class Jumia(models.Model):
    name = models.TextField()
    price = models.IntegerField()
    discount = models.IntegerField()
    #url = models.URLField(max_length=200)
    
    def __str__(self):
        return self.name
class Perfecto(models.Model):
    name = models.TextField()
    price = models.IntegerField()
    discount = models.IntegerField()
    link = models.URLField(max_length=200)
    
    def __str__(self):
        return self.name