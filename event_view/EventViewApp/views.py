from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.forms.models import model_to_dict
from django.db.models import Q

from .models import Event
from .forms import EventForm

from django.contrib.auth.decorators import login_required

from datetime import date, timedelta
import calendar
from itertools import chain

@login_required
def event_view(request):
    today = date.today()
    events = Event.objects.filter(end_date__gte=today)
    context = {
        'events': events
    }
    return render(request, 'EventViewApp/event_view.html', context)

@login_required
def event_view_achive(request):
    today = date.today()
    events = Event.objects.filter(end_date__gte=today-timedelta(days=7))
    context = {
        'events': events
    }
    return render(request, 'EventViewApp/event_view.html', context)

def get_last_date(dt):
    return dt.replace(day=calendar.monthrange(dt.year, dt.month)[1])

def get_first_date(dt):
    return dt.replace(day=1)

@login_required
def event_calendar(request):
    today = date.today()
    events = [ {
            'title': event.title,
            'start': event.start_date.strftime("%Y-%m-%d"),
            'end':event.end_date.strftime("%Y-%m-%d")
        }
        for event in  Event.objects.exclude(Q(end_date__lte=get_first_date(today)) | Q(start_date__gte=get_last_date(today)))
        ]
    context = {
        'event': events
    }
    return render(request, 'EventViewApp/calendar.html', context)


@login_required
def event_delete(request, event_id):
    try:
        event = Event.objects.get(pk=event_id)
        event.delete()
    except Event.DoesNotExist:
        raise Http404("Event does not exist")
    return redirect('/eventview/')

@login_required
def event_add(request):
    event = Event()
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/eventview/')
        else:
            print("ERROR FORM INVALID")
    context = {
        'event': event,
        'periods': Event.PERIOD_CHOICE
    }
    return render(request, 'EventViewApp/edit.html', context)

@login_required
def event_edit(request, event_id):
    try:
        event = Event.objects.get(pk=event_id)
    except Event.DoesNotExist:
        raise Http404("Event does not exist")
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/eventview/')
        else:
            print("ERROR FORM INVALID")
    context = {
        'event': event,
        'periods': Event.PERIOD_CHOICE
    }
    return render(request, 'EventViewApp/edit.html', context)
