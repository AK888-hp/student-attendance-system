from django.db import models

# Create your models here.
class Student(models.Model):
    student_id=models.CharField(max_length=20,primary_key=True)
    name=models.CharField(max_length=20)
    email=models.EmailField(unique=True)
    attendance_count=models.IntegerField(default=0)
    def __str__(self):
        return self.name

class Attendance(models.Model):
    student=models.ForeignKey("Student", on_delete=models.CASCADE)
    date = models.DateField()
    percentage = models.FloatField()
    
    def __str__(self):
        return self.name