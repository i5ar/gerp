from django.shortcuts import render
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.urls import reverse

from registration.backends.default.views import RegistrationView

from .forms import MemberRegistrationForm, UserForm, MemberForm, BiographyForm
from .models import Member


# http://stackoverflow.com/questions/29620940/django-registration-redux-add-extra-field/
class MemberRegistrationView(RegistrationView):

    form_class = MemberRegistrationForm

    def register(self, form_class):
        new_user = super(MemberRegistrationView, self).register(form_class)

        # NOTE: Add membership attribute
        member = Member.objects.create(
            user=new_user,
            membership=form_class.cleaned_data['membership'],
        )
        member.save()

        # NOTE: Add user to group
        group, created = Group.objects.get_or_create(name='Member')
        group.user_set.add(new_user)

        return new_user


@login_required
def index(request):
    member = get_object_or_404(Member, user_id=request.user)
    context = {'member': member}
    return render(request, 'accounts/profile.html', context)


@login_required
def edit(request):
    '''
    Update all profile fields.
    '''
    # NOTE: More forms in a page require specific URL in the form action.
    try:
        form_user = UserForm(instance=request.user)
        form_member = MemberForm(instance=request.user.member)
        form_biography = BiographyForm(instance=request.user.biography)

    except:
        form_user = UserForm
        form_member = MemberForm
        form_biography = BiographyForm

    context = {
        'form_user': form_user,
        'form_member': form_member,
        'form_biography': form_biography,
    }

    # Render
    # https://docs.djangoproject.com/en/1.8/topics/http/shortcuts/#render
    # return render_to_response(
    #     'accounts/jumbotron-edit.html',
    #     context,
    #     context_instance=RequestContext(request))
    return render(request, 'accounts/edit.html', context)


@login_required
def edit_user(request):
    '''Update User Fields'''
    if request.method == 'POST':
        form_user = UserForm(
            request.POST, instance=request.user)
        if form_user.is_valid():
            form_user.save()
            return HttpResponseRedirect(reverse('profile:index'))
    else:
        try:
            form_user = UserForm(instance=request.user)
        except:
            form_user = UserForm

    context = {'form_user': form_user}

    return render(request, 'accounts/edit.html', context)


@login_required
def edit_member(request):
    '''Update Member Fields'''
    if request.method == 'POST':
        form_member = MemberForm(
            request.POST, instance=request.user.member)
        if form_member.is_valid():
            form_member.save()
            return HttpResponseRedirect(reverse('profile:index'))
    else:
        try:
            form_member = MemberForm(instance=request.user.member)
        except:
            form_member = MemberForm

    context = {'form_member': form_member}

    return render(request, 'accounts/edit.html', context)


@login_required
def edit_biography(request):
    '''Update Biography Fields'''
    if request.method == 'POST':
        form_biography = BiographyForm(
            request.POST, instance=request.user.biography)
        if form_biography.is_valid():
            form_biography.save()
            return HttpResponseRedirect(reverse('profile:index'))
    else:
        try:
            form_biography = BiographyForm(instance=request.user.biography)
        except:
            form_biography = BiographyForm

    context = {'form_biography': form_biography}

    return render(request, 'accounts/edit.html', context)


def detail(request, username):
    '''Get objects from database'''
    user_id = get_object_or_404(User, username=username).pk
    member = get_object_or_404(Member, user_id=user_id)
    context = {'member': member}
    return render(request, 'accounts/detail.html', context)
