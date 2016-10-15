from django.db import models
from adminacc.models import Question

# Create your models here.
class ClUser(models.Model):
	uname = models.CharField(max_length=20,primary_key=True)
	pword = models.CharField(max_length=40)
	voters_id = models.CharField(max_length=100)

class PollQuestion(models.Model):
	user = models.ForeignKey(ClUser)
	question = models.ForeignKey(Question,primary_key=False)
	option = models.IntegerField(blank=True,default=0)