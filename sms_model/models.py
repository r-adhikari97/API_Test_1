from django.db import models


# Create your models here.
class SMS(models.Model):
    header = models.CharField(max_length=9, blank=False, null=False)
    tsp = models.CharField(max_length=1,blank=False,null=False,default="ZZZZ")
    oap = models.CharField(max_length=1,blank=False,null=False,default="ZZZZ")
    is_bank = models.BooleanField(default=False)
    body = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self):
        return self.header

# Templates class : Stores Template Signatures : One to Many with SMS
