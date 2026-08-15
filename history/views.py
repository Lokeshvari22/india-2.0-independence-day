from django.shortcuts import render, get_object_or_404

from .models import HistoricalEvent


def timeline(request):

    events = HistoricalEvent.objects.all()

    return render(
        request,
        "history/timeline.html",
        {
            "events": events
        }
    )


def event_detail(request, event_id):

    event = get_object_or_404(
        HistoricalEvent,
        id=event_id
    )

    return render(
        request,
        "history/event_detail.html",
        {
            "event": event
        }
    )