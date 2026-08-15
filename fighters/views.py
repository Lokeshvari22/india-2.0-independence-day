from django.shortcuts import render, get_object_or_404

from .models import FreedomFighter


def fighter_list(request):

    fighters = FreedomFighter.objects.all()

    return render(
        request,
        "fighters/fighter_list.html",
        {
            "fighters": fighters
        }
    )


def fighter_detail(request, fighter_id):

    fighter = get_object_or_404(
        FreedomFighter,
        id=fighter_id
    )

    return render(
        request,
        "fighters/fighter_detail.html",
        {
            "fighter": fighter
        }
    )


def random_fighter(request):

    fighter = (
        FreedomFighter.objects
        .order_by("?")
        .first()
    )

    return render(
        request,
        "fighters/random_fighter.html",
        {
            "fighter": fighter
        }
    )