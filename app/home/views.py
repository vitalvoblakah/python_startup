from django.shortcuts import render

# Create your views here.
from utils.utils import render_template

from authentication.models import User


def home(request):
    users = User.objects.all().exclude(pk=request.user.pk)

    return render_template(request, 'home.html', {'users': users})

