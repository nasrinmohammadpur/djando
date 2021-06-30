from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    class Meta:
        verbose_name="کاربر"
        verbose_name_plural="کاربر"
    
    user= models.OneToOneField(User,on_delete=models.CASCADE,verbose_name="کاربری")
    phone= models.IntegerField()  
    name= models.CharField(max_length=100,verbose_name="نام") 
    family= models.CharField(max_length=100,verbose_name="نام خانوادگی") 
    #image= models.imageField(upload_to="profileimage/",verbose_name="عکس")

    man=1
    woman=2
    status_choices=(("man","مرد"),("woman","زن"))
    gender=models.IntegerField(choices=status_choices,verbose_name="جنسیت")
    credit=models.IntegerField(verbose_name="اعتبار",default=0)


    def __str__(self):
        return "fullname:{} {}" .format(name,family)
