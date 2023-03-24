from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)
    maxtasks = models.IntegerField(default=20)
    def __str__(self) -> str:
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=500)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return  self.project.name +' - ' + self.title 