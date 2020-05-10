from django.db import models

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=32, verbose_name='名称')


class ProjectInfo(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='图片')
    # image = models.FileField(upload_to='media/images/%Y/%m/%d')


class Image(models.Model):
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    image = models.FileField(upload_to='media/images/%Y/%m/%d')