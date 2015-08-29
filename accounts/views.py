from __future__ import unicode_literals
import json
from django.shortcuts import render
from django.views.generic import View
from django.core.context_processors import csrf 
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from utils.login_require import LoginRequiredMixin

from .forms import RegistrationForm,LoginForm,UserProfileForm
from .models import UserProfile
from tag.models import Tag
# Create your views here.

class RegisterView(View):
    def get(self, request):
        args={}
        args.update(csrf(request))
        form=RegistrationForm()
        args['form']=form
        return render(request, 'registration.html',args)

    def post(self, request):
        form = RegistrationForm(data=request.POST)        
        if form.is_valid():
            form.save()
            user = authenticate(username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'])
            login(request, user)            
            return HttpResponseRedirect(reverse('user:register_success'))
        else:
            args={}
            args.update(csrf(request))
            args['form']=form
            return render(request, 'registration.html',args)
class RegisterSuccessView(View):
    def get(self, request):
        return render(request, 'registration_success.html',{})

class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated():
            return HttpResponseRedirect(reverse('index'))
        args={}
        args.update(csrf(request))
        form=LoginForm()
        args['form']=form
        return render(request, 'login.html', args)

    def post(self, request):
        args={}
        form=LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is None:
                user=User.objects.get(email=form.cleaned_data['username'])
                if user is not None and user.check_password(form.cleaned_data['password']):                    
                    user=authenticate(username=user.username, password=form.cleaned_data['password'])
                else:
                    user=None
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('index'))
                else:
                    args['message']='User is inactive'
            else:
                args['message']='Log in detail is incorrect'           
        args['form']=form
        return render(request,'login.html',args)
class LogoutView(LoginRequiredMixin,View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('index'))

class ProfileView(View):
    def get(self, request, username=None):
        args={}
        if username:
            #profile of another user
            try:
                user=User.objects.get(username=username)
                if user==request.user:
                    return HttpResponseRedirect(reverse('user:myprofile'))
                profile=user.profile
                args['profile']=profile
            except User.DoesNotExist:
                pass                
        else:
            #my profile
            if request.user.is_authenticated():
                profile=request.user.profile
                followers=profile.followers.all()
                follows=profile.follows.all()
                args['followers']=followers
                args['follows']=follows
                args['profile']=profile
            else:
                return HttpResponseRedirect(reverse('user:login'))
        args.update(csrf(request))        
        return render(request,'profile_index.html',args)

class EditProfileView(LoginRequiredMixin,View):
    def get(self,request):
        profile=UserProfile.objects.get(user=request.user)
        form=UserProfileForm(instance=profile)
        args={}
        args.update(csrf(request))
        args['form']=form
        return render(request,'editprofile.html',args)

    def post(self,request):
        form=UserProfileForm(request.POST,request.FILES,instance=request.user.profile)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('user:myprofile'))
        else:
            args={}
            args.update(csrf(request))
            args['form']=form
            return render(request,'editprofile.html',args)

class FollowUser(View):
    def post(self,request):
        message={}
        if request.user.is_authenticated():
            username=request.POST.get('username','')
            if username:
                try:
                    user=User.objects.get(username=username)
                    if user.profile not in request.user.profile.follows.all():
                        request.user.profile.follows.add(user.profile)
                        request.user.profile.save()
                        user.profile.rank+=0.05
                        user.profile.save()
                        message['status']='OK'
                        message['message']=''
                        message['followers_count']=user.profile.followers_count
                        message['label']='Unfollow'
                    else:
                        request.user.profile.follows.remove(user.profile)
                        request.user.profile.save()
                        user.profile.rank-=0.05
                        user.profile.save()
                        message['status']='OK'
                        message['followers_count']=user.profile.followers_count
                        message['label']='Follow'
                        message['message']=''
                except User.DoesNotExist:
                    message['status']='False'
                    message['message']='user not exit'       
        else:
            message['message']='You must login first'
            message['status']='False'
        return HttpResponse(json.dumps(message), content_type = "application/json")

class FollowTag(View):
    def post(self,request):
        message={}
        if request.user.is_authenticated():
            tagid=request.POST.get('tagid','')
            if tagid:
                try: 
                    tag=Tag.objects.get(pk=tagid)
                    if request.user.profile not in tag.tag_followers.all():
                        #follow
                        request.user.profile.follow_tags.add(tag)
                        request.user.profile.save()
                        tag.save()
                        message['status']='OK'
                        message['message']=''
                        message['followers_count']=tag.followers_count
                        message['label']='Unfollow'
                    else:
                        #unfollow
                        request.user.profile.follow_tags.remove(tag)
                        request.user.profile.save()
                        tag.save()
                        message['status']='OK'
                        message['message']=''
                        message['followers_count']=tag.followers_count
                        message['label']='Follow'
                except Tag.DoesNotExist:
                    message['status']='False'
                    message['message']='Tag is not exit'
            else:
                message['message']='Tagid is invalid'
                message['status']='False'
        else:
            message['message']='You must login first'
            message['status']='False'
        return HttpResponse(json.dumps(message), content_type = "application/json")

class ChangePasswordView(LoginRequiredMixin,View):
    pass