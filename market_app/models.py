from django.db import models

class JSONData(models.Model):
    date = models.DateField()
    trade_code = models.CharField(max_length=20)
    high = models.FloatField()
    low = models.FloatField()
    open = models.FloatField()
    close = models.FloatField()
    volume = models.IntegerField()

    def __str__(self):
        return self.trade_code
