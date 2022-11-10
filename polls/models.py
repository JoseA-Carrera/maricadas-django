from django.db import models

class Priorities(models.Model): 
    date = models.CharField(max_length=100, blank=True, null=True)

    urgent_count = models.SmallIntegerField(blank=True, null=True) 
    urgent_time = models.FloatField(blank=True,null=True) 

    high_count = models.SmallIntegerField(blank=True, null=True) 
    high_time = models.FloatField(blank=True,null=True) 

    normal_count = models.SmallIntegerField(blank=True,null=True) 
    normal_time = models.FloatField(blank=True,null=True)

    low_count = models.SmallIntegerField(blank=True,null=True) 
    low_time = models.FloatField(blank=True,null=True)