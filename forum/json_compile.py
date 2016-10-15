from forum.models import Forum
from adminacc.models import Question

def compile_qn(questions):
	question_aslist = []
	question_asdict = {}
	for each in questions:
		thread_dict = dict()
		thread_dict['id'] = each.qid
		thread_dict['question'] = each.question
		thread_dict['comments'] = each.comments
		thread_dict['polls'] = each.activity
		question_aslist.append(thread_dict)
	question_asdict = {'threads': question_aslist}
	return question_asdict

def compile_thread(thread,pollqn):
	thread_list = []
	for each in thread:
		msg_object = dict()
		msg_object['user'] = each.user.uname
		msg_object['text'] = each.answers
		msg_object['timestamp'] = each.timestamp
		thread_list.append(msg_object)
	msg_dict = {'messages':thread_list,'chosen':pollqn.option,'options':pollqn.question.polls}
	print msg_dict
	return msg_dict

def compile_thread_admin(thread):
	thread_list = []
	for each in thread:
		msg_object = dict()
		msg_object['user'] = each.user.uname
		msg_object['text'] = each.answers
		msg_object['timestamp'] = each.timestamp
		thread_list.append(msg_object)
		msg_dict = {'messages':thread_list}
	return msg_dict


def compile_broadcast(broadcasts):
	broad_list = []
	for each in broadcasts:
		announcement = dict()
		announcement['announcement']= each.message
		announcement['timestamp'] = each.timestamp
		broad_list.append(announcement)
	broad_dict = {'announcements':broad_list}
	return broad_dict