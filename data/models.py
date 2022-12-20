from django.db import models
class data(models.Model):
    fname=models.TextField()
    lname=models.TextField()
    rno=models.TextField()
    dept=models.TextField()
    problem=models.TextField()
    desc=models.TextField()



