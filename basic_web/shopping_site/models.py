from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=128)
    price = models.IntegerField(null=True, blank=True)
    amount = models.IntegerField(null=True, blank=True)
    status = models.BooleanField(default=0)
    update_time = models.DateTimeField('更新時間', null=True,auto_now=True)
    create_time = models.DateTimeField(null=True,auto_now_add=True)

    def __str__(self):
        return self.name