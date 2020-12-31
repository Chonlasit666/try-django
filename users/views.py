from django.shortcuts import render
from django.http import HttpResponse

from .models import User

# Create your views here.
def index(request):
    latest_username_list = User.objects.order_by('-pub_date')[:5]
    output =', '.join([q.username for q in latest_username_list])
    return HttpResponse(output)


def detail(request, user_id):
    return HttpResponse("You're looking at username %s." % user_id)
