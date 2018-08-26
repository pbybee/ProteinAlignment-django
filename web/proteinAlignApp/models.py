from django.db import models

# Create your models here.
class Align(models.Model):
	align = models.TextField()
	reference = models.TextField()
	alignedV = models.TextField()
	alignedW = models.TextField()
