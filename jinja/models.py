from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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
    date_added=models.DateTimeField(default=timezone.now)
    type=models.CharField(max_length=2,choices=CHAI_TYPE_CHOICE,default='MS')
    description=models.TextField(default='This is a chai variety')
    price=models.DecimalField(max_digits=5,decimal_places=2,default=100)
    
    
    def __str__(self):
        return self.name
    



# one to many  relationship
# one chai variety can have multiple reviews




class chaiReview(models.Model):
    chai =models.ForeignKey(ChaiVariety, on_delete=models.CASCADE, related_name='reviews')
#     on delete cascade mantains the refrential integrity , 
# for example we have a parent model/table named "employee" and it has 2 child tables/models i.e "salary" or "dependent" 
# lets assume that we make some changes in employee table , or employee 34 has left the company , so logically his data from the salary and dependent table should also be removed, 
# here comes the "on_delete=models.CASCADE" which  deletes the data from the child tables, and thus mantains the refrential integrity of the database.
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    rating=models.IntegerField()
    comment=models.TextField()
    date_added=models.DateTimeField(timezone.now)
    def __str__(self):
         return f'{self.user.username} review on {self.chai.name}'






# many to many relationship 
#  one chai can be on multiple stores and one store can have multiple chai

class store(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    chai_varities=models.ManyToManyField(ChaiVariety, related_name='stores')
    # related name is used for , k dosry table ma main kis name sy jana jaaon 
    def __str__(self):
        return self.name
    



# one to one relationship
# one chai variety can have one tea bag or one certificate can only be given to one chai 
class chaiCertificates(models.Model):
    chai=models.OneToOneField(ChaiVariety,on_delete=models.CASCADE, related_name='certificates')
    certificate_number=models.CharField(max_length=100)
    issued_date=models.DateTimeField(default=timezone.now)
    valid_till=models.DateTimeField()
    def __str__(self):
        return f'certificate for {self.chai.name}'