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
    Categories = models.ForeignKey('Category',on_delete=models.CASCADE)


    def __str__(self):
        return  self.title
    


class Category (models.Model):
        name = models.CharField(max_length=25)

         
        def __str__(self):
            return self.name
# Create your models here.
