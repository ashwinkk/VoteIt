from django.shortcuts import render
from django.http import JsonResponse
from forum.models import Forum
from adminacc.models import Question,Announcements
from users.models import ClUser,PollQuestion
from .json_compile import compile_qn,compile_thread,compile_broadcast,compile_thread_admin
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def serve_forum_threads(request):
	questions = Question.objects.all()
	print questions
	qdict = compile_qn(questions)
	print qdict
	return JsonResponse(qdict)

@csrf_exempt
def thread(request,t_id):
	print "Gege"
	message_list = {'fafa':'Fafaf'}
	thread_id = int(t_id)
	packet = json.loads(request.body)
	# packet = request.POST
	if(packet['view']==False):
		message = packet['message']
		user = packet['user']
		newuser = ClUser.objects.all().filter(uname=user)[0]
		qn = Question.objects.all().filter(qid=t_id)[0]
		pollres = PollQuestion.objects.all().filter(question=qn,user=newuser)
		if len(pollres)==0:
			print "hee"
			poll = PollQuestion(user=newuser,question=qn)
			poll.save()
		qn.comments = qn.comments+1
		qn.save()
		forum = Forum(thread=qn,user=newuser,answers=message)
		forum.save()
		return JsonResponse({'status':True})
	else:
		print "here"
		user = packet['user']
		message_list['m']='n';
		if not(user=='admin'):
			newuser = ClUser.objects.all().filter(uname=user)[0]
			qn = Question.objects.all().filter(qid=t_id)[0]
			pollqn =  PollQuestion.objects.all().filter(user = newuser,question=qn)
			thread = Forum.objects.all().filter(thread=qn)
			if (thread and len(pollqn)>0):
				message_list = compile_thread(thread,pollqn[0])
				message_list['m'] = 'y'
			if(len(pollqn)>0):
				pollqn=pollqn[0]
				message_list['chosen'] = pollqn.option
				message_list['option'] = pollqn.question.polls
		else:
			qn = Question.objects.all().filter(qid=t_id)[0]
			thread = Forum.objects.all().filter(thread=qn)
			if(thread):
				message_list = compile_thread_admin(thread)	
				message_list['m'] = 'y'
		print message_list
	return JsonResponse(message_list)

@csrf_exempt
def announcements(request):
	broadcasts = Announcements.objects.all()
	broadcast_dict = compile_broadcast(broadcasts)
	return JsonResponse(broadcast_dict)