from django.core import serializers
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse
from django.forms.models import model_to_dict
from django.db.models import Q

from .models import Event, Info
from .forms import EventForm

from django.contrib.auth.decorators import login_required

from datetime import date, timedelta
import calendar
from itertools import chain

@login_required
def event_view(request):
    today = date.today()
    events = Event.objects.filter(end_date__gte=today).order_by('end_date')

    # お知らせ用モーダル表示情報を取得
    info, created = Info.objects.get_or_create(identifier='update-info')

    # 表示に必要な情報を付与
    for e in events:
        # New か Update を付与する
        if today < e.last_update + timedelta(days=3):
            if e.created_at == e.last_update:
                e.freshness_tag = 'New'
            else:
                e.freshness_tag = 'Update'
        else:
            e.freshness_tag = ''
        # 残り日数を計算
        e.left_date = (e.end_date - date.today()).days

    context = {
        'periods' : [p[1] for p in Event.PERIOD_CHOICE],
        'events': events,
        'info': info
    }
    return render(request, 'EventViewApp/event_view.html', context)

@login_required
def event_view_achive(request):
    today = date.today()
    events = Event.objects.filter(end_date__gte=today-timedelta(days=7))
    info, created = Info.objects.get_or_create(identifier='update-info')

    for e in events:
        # 残り日数を計算
        e.left_date = (e.end_date - date.today()).days

    context = {
        'periods' : [p[1] for p in Event.PERIOD_CHOICE],
        'events': events,
        'info': info
    }
    return render(request, 'EventViewApp/event_view.html', context)

# 月の最終日の日付を返す
def get_last_date(dt) -> date:
    return dt.replace(day=calendar.monthrange(dt.year, dt.month)[1])

# 月の最初の日付を返す
def get_first_date(dt) -> date:
    return dt.replace(day=1)

# カレンダー表示
@login_required
def event_calendar(request):
    # カレンダー表示の際の帯の色
    colors = {
        1: '#3399ff',
        2: '#ff5252',
        3: '#b8cc00',
        4: '#ff5cf7',
        5: '#138496',
        6: '#53cc52',
        7: '#a284ff',
        8: '#df6400',
        9: '#4c94ff'
    }
    today = date.today()
    end_date = get_first_date(today)-timedelta(days=7)
    start_date = get_last_date(today)+timedelta(days=7)
    events = [ {
            'title': event.title,
            'overview': event.overview,
            'id' : event.id,
            'start': event.start_date.strftime("%Y-%m-%d"),
            'end':event.end_date.strftime("%Y-%m-%d"),
            'color': colors.get(event.period),
            }
        for event in  Event.objects.exclude(Q(end_date__lte=end_date) | Q(start_date__gte=start_date))
        ]
    context = {
        'event_data': events
    }
    return render(request, 'EventViewApp/calendar.html', context)

# ajax 形式でイベント内容を取得する
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

@login_required
def update_info_save(request):
    info_id = request.POST.get('id')
    content = request.POST.get('content')
    update_info= Info.objects.filter(pk=info_id)
    update_info.update(
        content = content
    )
    return JsonResponse(serializers.serialize("json", update_info), safe=False)