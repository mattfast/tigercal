from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect

def index(request):
    return render(request, 'index.html')

def publicevents(request):
	events = Event.objects.filter(is_public=True)
	context = {'events': events}
	return render(request, 'publicevents.html', context)

def events(request, group_id):
	group = get_object_or_404(Group, pk=group_id)
	events = Event.objects.filter(group=group)
	context = {'events': events}
	return render(request, 'events.html', context)

def groupform(request):
	return render(request, 'groupform.html')

def makegroup(request):
	try:
		name = request.POST['name']
		group = Group.objects.create(name=name)
	except:
		context = {'error_message': 'You must enter a group name.'}
		return render(request, 'groupform.html', context)

	return HttpResponseRedirect(reverse(events, args = (group.id,)))

