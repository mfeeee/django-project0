from django.db import models
from django.contrib.auth.models import User
from users.models import User
from datetime import datetime

# Create your models here.
class Courses(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField()
    thumb = models.ImageField(upload_to = "thumb_courses")

    def __str__(self) -> str:
        return self.name

class Classes(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField()
    grade = models.FileField(upload_to = "grade")
    course = models.ForeignKey(Courses, on_delete = models.DO_NOTHING)

    def __str__(self) -> str:
        return self.name

class Comments(models.Model):
    user = models.ForeignKey(User, on_delete= models.DO_NOTHING)
    comment = models.TextField()
    date = models.DateTimeField(default = datetime.now)
    classes = models.ForeignKey(Classes, on_delete= models.DO_NOTHING)

    def __str__(self) -> str:
        return self.user.name