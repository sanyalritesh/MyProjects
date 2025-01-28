from django.db import models

# Create your models here.



class sendmail(models.Model):
    address = models.EmailField(max_length=254, unique=True)
    file = models.FileField(upload_to='files/')
    subject=models.TextField(null=True,blank=False)
    message=models.TextField(null=True,blank=False)
