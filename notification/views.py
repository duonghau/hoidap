from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import View
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from utils.login_require import LoginRequiredMixin
from .models import Notification
# Create your views here.

class NewNotificationsView(LoginRequiredMixin,View):
    def get(self, request):
        args={}
        notifications=Notification.objects.filter(recipient=request.user.profile, is_read=False).order_by('-create')
        if len(notifications) < 10:
            notifications=Notification.objects.filter(recipient=request.user.profile).order_by('-create')[:10]
        args['notifications']=notifications
        return render(request, 'new_notification.html',args)

class AllNotificationsView(LoginRequiredMixin, View):
    def get(self, request):
        notifications=Notification.objects.all().order_by('-create')[:30]
        args={}
        args['notifications']=notifications
        return render(request, 'all_notification.html',args)

class ViewNotificationView(LoginRequiredMixin,View):
    def get(self,request,notificationid):        
        try:
            notification=Notification.objects.get(pk=notificationid)
            if not notification.is_read:                
                notification.is_read=True
                notification.save()
        except ObjectDoesNotExist:            
            pass
        return HttpResponseRedirect(notification.notification_url)

class MarkAllReadView(LoginRequiredMixin, View):
    def get(self, request):
        notifications=Notification.objects.filter(recipient=request.user.profile, is_read=False)
        if notifications:
            for notification in notifications:
                notification.is_read=True
                notification.save()
        notifications=Notification.objects.filter(recipient=request.user.profile).order_by('-create')[:10]
        args={}
        args['notifications']=notifications
        return render(request, 'new_notification.html',args)