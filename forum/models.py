from django.db import models
from users.models import ClUser
from adminacc.models import Question

# Create your models here.

class Forum(models.Model):
	thread = models.ForeignKey(Question)
	answers = models.CharField(max_length=1000)
	timestamp = models.DateField(auto_now=True)
	user = models.ForeignKey(ClUser)