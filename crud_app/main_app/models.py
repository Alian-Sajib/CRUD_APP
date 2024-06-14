from django.db import models

class stock(models.Model):
    date = models.DateField() 
    trade_code = models.CharField(max_length=50)
    high = models.CharField(max_length=50)
    low =models.CharField(max_length=50)
    open =models.CharField(max_length=50)
    close = models.CharField(max_length=50)
    volume = models.CharField(max_length=50)
    class Meta:
        ordering =['-date']

    def __str__(self):
        return self.trade_code