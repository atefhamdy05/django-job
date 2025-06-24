from django.db import models
JOB_TYPE = (
    ('Full TIME','Full TIME'),
    ('PART TIME','PART TIME'),

)
class job(models.Model):
    title = models.CharField(max_length=100)
    JOB_Type = models.CharField(max_length=100,choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    published_ate = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=0)
# Create your models here.
