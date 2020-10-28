from django.core import serializers
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse
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
    for e in events:
        if today < e.last_update + timedelta(days=7):
            e.is_new = True
        else:
            e.is_new = False
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
    colors = {
        1: '#3399ff',
        2: '#ff5252',
        3: '#d0e226',
        4: '#18aa1d'
    }
    today = date.today()
    events = [ {
            'title': event.title,
            'id' : event.id,
            'start': event.start_date.strftime("%Y-%m-%d"),
            'end':event.end_date.strftime("%Y-%m-%d"),
            'color': colors.get(event.period),
            }
        for event in  Event.objects.exclude(Q(end_date__lte=get_first_date(today)) | Q(start_date__gte=get_last_date(today)))
        ]
    context = {
        'event_data': events
    }
    return render(request, 'EventViewApp/calendar.html', context)

@login_required
def ajax_get_event(request):
    event_id = request.POST.get('event_id')
    event = Event.objects.filter(pk=event_id)
    return JsonResponse(serializers.serialize("json", event), safe=False)


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
