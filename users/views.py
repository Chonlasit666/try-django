from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse

from .models import User

# Create your views here.
def index(request):
    latest_username_list = User.objects.order_by('-pub_date')[:5]
    context = {'latest_username_list': latest_username_list}
    return render(request, 'users/index.html', context)


def detail(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'users/detail.html', {'user': user})

