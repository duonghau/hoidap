from django.shortcuts import render
from django.views.generic import View
from .models import Conversation, Message,MessageReadState
from utils.login_require import LoginRequiredMixin

# Create your views here.
class AllConversationView(LoginRequiredMixin,View):
    pass

class SendMessageView(LoginRequiredMixin,View):
    pass

class ConversationView(LoginRequiredMixin,View):
    pass
