# from django.db import models
from django.db import models

#login調整介面的
class ButtonConfig(models.Model):
    position_x = models.IntegerField(default=50)
    position_y = models.IntegerField(default=50)
    width = models.IntegerField(default=50)
    height = models.IntegerField(default=50)

# Create your models here.
