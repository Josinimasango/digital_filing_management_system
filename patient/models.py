from django.db import models

GENDER_CHOICES=(
    ('male','MALE'),
    ('female','Female'),
    ('other','Other'),
)
class Patient(models.Model):
    name=models.CharField(max_length=200)
    age=models.IntegerField(default=0)
    gender=models.CharField(choices=GENDER_CHOICES,default='male')
    mobile=models.IntegerField(null=True)
    address=models.TextField(null=True)
    Detail=models.TextField(null=True)
    medicine_detail=models.TextField(null=True)
    note=models.TextField(null=True)
    next_visit=models.TextField(default=0)
