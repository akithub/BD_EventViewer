from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.forms.models import model_to_dict

from .models import Event
from .forms import EventForm


def event_view(request):
    events = Event.objects.all()
    context = {
        'events': events
    }
    return render(request, 'EventViewApp/event_view.html', context)



def event_add(request):
    event = Event()
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        else:
            print("ERROR FORM INVALID")
            for elm in form:
                print(elm)
    context = {
        'event': event
    }
    return render(request, 'EventViewApp/edit.html', context)

def event_edit(request, event_id):
    try:
        event = Event.objects.get(pk=event_id)
    except Event.DoesNotExist:
        raise Http404("Event does not exist")
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save(commit=True)
        else:
            print("ERROR FORM INVALID")
            for elm in form:
                print(elm)
    context = {
        'event': event,
        'periods': Event.PERIOD_CHOICE
    }
    return render(request, 'EventViewApp/edit.html', context)
