from django.shortcuts import render
from django.http import JsonResponse
from .models import Question
from users.models import PollQuestion,ClUser
from forum.models import Forum
from adminacc.models import Announcements
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def addQuestion(request):
	qndata = json.loads(request.body)
	# qndata  = request.POST
	qn = qndata['question']
	options = qndata['options']
	myqn = Question(question = qn,polls = options)
	myqn.save()
	user = ClUser.objects.all().filter(uname='vaanam')[0]
	user.save()
	foru = Forum(thread=myqn,answers="welcome!",user=user)
	foru.save()
	return JsonResponse({'status':True})

@csrf_exempt
def announce(request):
	broadcast = json.loads(request.body)
	# broadcast = request.POST
	message = broadcast['message']
	bmessage = Announcements(message=message)
	bmessage.save()
	return JsonResponse({'status':True})

@csrf_exempt
def summary(request):
	qns = Question.objects.all()
	count = 0
	question_list = []
	for each in qns:
		quest = dict()
		quest['comments'] = each.comments
		quest['question'] = each.question
		quest['polls'] = each.activity
		question_list.append(quest)
	details = {'summary':question_list}
	return JsonResponse(details)


@csrf_exempt
def chartdata(request):
	chdata = json.loads(request.body)
	# chdata = request.POST
	qdata = chdata['id']
	question = Question.objects.all().filter(qid=qdata)[0]
	users = PollQuestion.objects.all()
	optionpolls = dict()
	choices = question.polls
	choices = choices.split('|')
	print choices
	for one in choices:
		optionpolls[one] = 0
	for user in users:
		key = choices[user.option-1]
		optionpolls[key] =optionpolls[key]+1
	return JsonResponse(optionpolls)