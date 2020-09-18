from django.shortcuts import render
from django.http import HttpResponse

from .models import Event


def event_view(request):
    events = Event.objects.all()
    context = {
        'events': events
    }
    return render(request, 'EventViewApp/event_view.html', context)


def event_edit(request):
    return HttpResponse("event edit page")
