from django.db import models

# Create your models here.
class Question(models.Model):
	qid = models.AutoField(primary_key=True)
	question = models.CharField(max_length=500)
	polls = models.CharField(max_length=500,blank=True)
	activity = models.IntegerField(default=0)
	comments = models.IntegerField(default=0)

class Announcements(models.Model):
	annid = models.AutoField(primary_key=True)
	message = models.CharField(max_length=1000)
	timestamp = models.DateField(auto_now=True)