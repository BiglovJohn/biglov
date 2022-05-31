from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.views import View, generic
from .models import Profile
from .forms import ProfileForm


class ProfileListView(generic.ListView):
    model = Profile
    template_name = 'app_users/profiles_list.html'
    context_object_name = 'profiles'
    queryset = Profile.objects.all()


class ProfileDetailView(generic.DetailView):
    model = Profile
    template_name = 'app_users/profile_detail.html'
    context_object_name = 'profile'
    queryset = Profile.objects.all()


class AnotherLogoutView(LogoutView):
    template_name = 'app_users/logout.html'


class AnotherLoginView(LoginView):
    template_name = 'app_users/login.html'


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/profile/create')
    else:
        form = UserCreationForm()
    return render(request, 'app_users/register.html', {'form': form})


class ProfileFormView(View):

    def get(self, request):
        profile_form = ProfileForm()
        return render(request, 'app_users/create_profile.html', context={'profile_form': profile_form})

    def post(self, request):
        context = {}
        if request.method == 'POST':
            profile_form = ProfileForm(request.POST, request.FILES)

            if profile_form.is_valid():
                profile = profile_form.save(commit=False)
                profile.nick_name = request.user
                obj = Profile.objects.create(**profile_form.cleaned_data)
                profile.save()
                obj.save()
                return HttpResponseRedirect('/profiles')
        else:
            profile_form = ProfileForm()
        context['form'] = profile_form
        return render(request, 'app_users/create_profile.html', context={'profile_form': profile_form})


class ProfileEditFromView(View):
    def get(self, request, profile_id):
        profile = Profile.objects.get(id=profile_id)
        profile_form = ProfileForm(instance=profile)
        return render(request, 'app_users/edit_profile.html', context={'profile_form': profile_form, 'profile_id': profile_id})

    def post(self, request, profile_id):
        profile = Profile.objects.get(id=profile_id)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)

        if profile_form.is_valid():
            profile.save()
        return render(request, 'app_users/edit_profile.html', context={'profile_form': profile_form, 'profile_id': profile_id})
