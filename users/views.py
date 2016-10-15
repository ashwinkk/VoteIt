from django.shortcuts import render
from .models import ClUser,PollQuestion
from adminacc.models import Question
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def chooseOption(request):
	optdata = json.loads(request.body)
	print optdata
	# optdata = request.POST
	option = long(optdata['option'])
	name = optdata['user']
	qnid = optdata['id']
	print qnid
	user = ClUser.objects.all().filter(uname=name)[0]
	qn = Question.objects.all().filter(qid = qnid)[0]
	poll = PollQuestion.objects.all().filter(user = user,question=qn)[0]
	print type(poll.option),type(option)
	if not(poll.option == option):
		poll.option = option
		poll.save()
		qn.activity = qn.activity+1
		qn.save()
	return JsonResponse({'status':True})

@csrf_exempt
def UserLogin(request):
	user_data = json.loads(request.body)
	uname = user_data['uname']
	pword = user_data['pword']
	votid = user_data['voters_id']
	user = ClUser(uname = uname,pword = pword,voters_id = votid)
	user.save()
	return JsonResponse({'status':True})