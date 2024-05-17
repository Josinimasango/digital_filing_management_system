from django.db import models

GENDER_CHOICES = (
    ('male', 'MALE'),
    ('female', 'Female'),
    ('other', 'Other'),
)

class Patient(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    gender = models.CharField(choices=GENDER_CHOICES, default='male', max_length=10)
    mobile = models.BigIntegerField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    detail = models.TextField(null=True, blank=True)
    medicine_detail = models.TextField(null=True, blank=True)
    note = models.TextField(null=True, blank=True)
    next_visit = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
