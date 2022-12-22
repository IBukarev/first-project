from django.shortcuts import render
from .models import Online
from .forms import OnlineForm


def index(request):
    return render(request, 'blog/index.html')


def contact(request):
    return render(request, 'blog/contact.html')


def online(request):
    if request.method == 'POST':
        form = OnlineForm(request.POST)
        if form.is_valid():
            form.save()
    form = OnlineForm()
    sms = Online.objects.order_by('-id')
    return render(request, 'blog/online.html', {'sms': sms, 'form': form})