# coding=utf-8
# from django.views.generic import TemplateView


# class AboutView(TemplateView):
#     template_name = "about.html"

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from questions.paginate import paginate
from questions.models import *

user_authorized = True
best_members = ["Best_member_%d" % i for i in range(5)]
username = 'Sergey'
popular_tags = Tag.objects.top()

default_context = {"user_authorized": user_authorized,
                   "username": username,
                   "popular_tags": popular_tags,
                   "best_members": best_members
                   }


def index(request):
    questions = Question.objects.all()

    context = paginate(questions, request.GET.get('page'))

    context.update(default_context)

    page_content = {
        'header_main': 'New Question',
        'header_additional': 'Hot Question',
        'header_additional_href': '/hot'
    }

    context.update(page_content)

    return render(request, 'main.html', context)


def hot(request):
    questions = Question.objects.popular()

    context = paginate(questions, request.GET.get('page'))

    context.update(default_context)

    page_content = {
        'header_main': 'Hot Question',
        'header_additional': 'New Question',
        'header_additional_href': '',
    }

    context.update(page_content)

    return render(request, 'main.html', context)


def question(request, question_id):
    qst = get_object_or_404(Question, id=question_id)
    context = {'question': qst}
    answers = qst.answer_set.all()

    context.update({'answers': answers})

    context.update(default_context)
    return render(request, 'questions.html', context)


def tag(request, tag):
    tag_1 = get_object_or_404(Tag, tag=tag)
    questions = tag_1.question.all()

    context = paginate(questions, request.GET.get('page'))

    context.update(default_context)

    page_content = {
        'header_main': tag,
    }

    context.update(page_content)

    return render(request, 'main.html', context)


def login(request):
    context = default_context
    return render(request, 'login.html', context)


def signup(request):
    context = default_context
    return render(request, 'registration.html', context)


def ask(request):
    context = default_context
    return render(request, 'ask.html', context)


def settings(request):
    context = default_context
    return render(request, 'settings.html', context)


def about(request):
    if request.method == 'GET':
        get_post_str = request.GET.urlencode().replace("&", "\n")

    elif request.method == 'POST':
        get_post_str = request.POST.urlencode()
    get_post = {'str': get_post_str}
    return render(request, "questions/about.html", get_post)


def get_post(request):
    if request.method == 'GET':
        return HttpResponse(request.GET.urlencode().replace("&", "<br>"))

    elif request.method == 'POST':
        return HttpResponse(request.POST.urlencode())
