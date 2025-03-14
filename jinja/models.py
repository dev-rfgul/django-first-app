from django.db import models
from django.utils import timezone

# Create your models here.
class ChaiVariety(models.Model):
    CHAI_TYPE_CHOICE=[
        ('BL','Black'),
        ('GR','Green'),
        ('WT','White'),
        ('OL','Oolong'),
        ('HB','Herbal'),
        ('MS','Masala'),
        ('CL','Chai Latte'),
        ('IC','Iced'),
        ('BB','Bubble'),
    ]
    name= models.CharField(max_length=100)
    image=models.ImageField(upload_to='images/')
    date_added=models.DateTimeField(timezone.now)
    type=models.CharField(max_length=2,choices=CHAI_TYPE_CHOICE,default='MS')
    description=models.TextField(default='This is a chai variety')
    price=models.DecimalField(max_digits=5,decimal_places=2,default=100)
    
    
    def __str__(self):
        return self.name