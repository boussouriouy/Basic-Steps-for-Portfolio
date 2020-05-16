from django.shortcuts import render,get_object_or_404,redirect
from .form import MembersForms
from .models import Member
# Create your views here.

def home_view(request):
    context = {

    }
    return render(request, 'home.html', context)


def about_view(request):
    context = {

    }
    return render(request, 'about.html', context)


def contact_view(request):
    context = {

    }
    return render(request, 'cont.html', context)


def information_view(request):
    context = {

    }
    return render(request, 'info.html', context)


def register_view(request):
    my_form = MembersForms(request.POST or None)
    if my_form.is_valid():
        my_form.save()
        my_form = MembersForms()

    context = {
        'form': my_form
    }
    return render(request, 'join.html', context)


def member_view(request, *args, **kwargs):
    queryset = Member.objects.all()
    context = {
        'object_list': queryset
    }

    return render(request, 'member_list.html', context)


def member_details(request, id):
    obj = Member.objects.get(id=id)

    context = {
        'object': obj,
    }

    return render(request, 'detail.html', context)