# messenger_chat/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import Message

User = get_user_model()

@login_required
def chat(request, username):
    receiver = User.objects.get(username=username)
    messages = Message.objects.filter(sender=request.user, receiver=receiver) | \
               Message.objects.filter(sender=receiver, receiver=request.user)
    messages = messages.order_by('timestamp')
    return render(request, 'chat.html', {'receiver': receiver, 'messages': messages})

@login_required
def send_message(request, username):
    if request.method == 'POST':
        receiver = User.objects.get(username=username)
        content = request.POST.get('content')
        message = Message.objects.create(sender=request.user, receiver=receiver, content=content)
        return redirect('chat', username=username)
    else:
        return HttpResponse("Invalid request method")
