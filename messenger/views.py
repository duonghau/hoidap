# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.db.models import Q
from django.db.models import ObjectDoesNotExist
from accounts.models import UserProfile
from .models import Conversation, Message
from utils.login_require import LoginRequiredMixin

# Create your views here.
class AllConversationView(LoginRequiredMixin,View):
    def get(self, request):
        return render(request,'conversation_all.html',{})

class SendMessageView(View):
    def post(self, request, username):
        args={}
        if request.user.is_authenticated():            
            user1=request.user.profile
            user2=UserProfile.objects.get(user__username=username)
            if user1 and user2:
                try:
                    conversation=Conversation.objects.get(Q(user_one=user1) & Q(user_two=user2)|Q(user_one=user2) & Q(user_two=user1))
                except ObjectDoesNotExist:
                    conversation=Conversation()
                    conversation.user_one=user1
                    conversation.user_two=user2
                    conversation.save()
                if conversation:
                    message=Message()
                    message.sender=user1
                    message.recipient=user2
                    message.content=request.POST.get('message','')
                    message.conversation=conversation
                    message.save()
                    args['status']="OK"
                    args['message']="" 
            else:
                args['status']="False"
                args['message']='Không tồn tại user'
        else:
            args['status']="False"
            args['message']='Bạn cần đăng nhập'
        return HttpResponse(json.dumps(args), content_type="application/json")

class ConversationView(LoginRequiredMixin,View):
    def get(self, request, username):
        args={}
        args['username']=username
        user1=request.user.profile
        user2=UserProfile.objects.get(user__username=username)
        if user1 and user2:
            try:
                conversation=Conversation.objects.get(Q(user_one=user1) & Q(user_two=user2)|Q(user_one=user2) & Q(user_two=user1))
                if conversation:           
                    messages=conversation.conversation_messages.all().order_by('create')
                    for message in messages:
                        if message.recipient==request.user.profile and message.read==None:
                            message.read=datetime.now()
                            message.save()
                    args['messages']=messages;
            except ObjectDoesNotExist:
                pass        
        return render(request, 'conversation.html',args)

class NewConversationView(LoginRequiredMixin,View):
    def get(self, request):
        args={}
        messages=Message.objects.filter(recipient=request.user.profile,read=None).order_by('-create')
        if len(messages)<5:
            messages=Message.objects.filter(recipient=request.user.profile).order_by('-create')[:5]
        args['messages']=messages
        return render(request, 'new_messages.html', args)

class NewMessageAjaxView(View):
    def get(self, request,username):
        userchat=UserProfile.objects.get(user__username=username)
        args={}
        messages=Message.objects.filter(recipient=request.user.profile,sender=userchat,read=None).order_by('create')
        for message in messages:
            message.read=datetime.now()
            message.save()
        args['messages']=messages
        return render(request, 'new_message_ajax.html', args)