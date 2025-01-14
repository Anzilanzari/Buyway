from django.db import models

# Create your models here.

from django.db import models

class Category(models.Model):
    cat_name=models.CharField(max_length=100)
    cat_icon=models.FileField(null=True,upload_to='images/',blank=True)
    def __str__(self):
        return self.cat_name
    

class Courses(models.Model):
    course = models.ForeignKey(Category,on_delete = models.CASCADE,null=True)
    course_name = models.CharField( max_length=100)
    course_instructor = models.CharField( max_length=100)
    course_rating = models.IntegerField(null=True)
    course_duration = models.CharField(max_length=500,null=True)
    course_price = models.IntegerField(null=True)
    course_description = models.CharField(max_length=500)
    course_languages = models.CharField(max_length=300)
    course_discount = models.IntegerField(null=True)
    course_thumbnail = models.ImageField(null=True,upload_to="images/",blank=True)
    course_cover = models.ImageField(null=True,upload_to="images/",blank=True)
    def __str__(self):
        return self.course_name
    
    def discounted_price(self):
        if self.course_discount and self.course_price:
            discount_amount = (self.course_price * self.course_discount) / 100
            return self.course_price - discount_amount
        return self.course_price
    