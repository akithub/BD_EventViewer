from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.forms.models import model_to_dict

from .models import Event
from .forms import EventForm, LoginForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import(LoginView, LogoutView)
from django.contrib.auth.decorators import login_required
from .forms import LoginForm

class Login(LoginView):
    form_class = LoginForm
    template_name = 'EventViewApp/login.html'


class Logout(LoginRequiredMixin, LogoutView):
    template_name = 'EventViewApp/login.html'

@login_required
def event_view(request):
    events = Event.objects.all()
    context = {
        'events': events
    }
    return render(request, 'EventViewApp/event_view.html', context)


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
