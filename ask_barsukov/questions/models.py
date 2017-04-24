# coding=utf-8
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User


class QuestionManager(models.Manager):
    def new(self):
        return self.all().order_by('-id')  # date?

    def popular(self):
        return self.all().order_by('-rating')


class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length=50)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, default=1)
    avatar = '/static/logo.svg'  # 11111111111111

    class Meta:
        ordering = ('-date',)
        verbose_name = u'вопрос'
        verbose_name_plural = u'вопросы'

    def get_tags(self):
        return self.tag_set.all()

    def get_answer_count(self):
        return self.answer_set.count()

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title


class Answer(models.Model):
    question = models.ForeignKey(Question, null=False)
    text = models.TextField()
    rating = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True, )
    approved = models.BooleanField(default=False)
    author = models.ForeignKey(User, default=1)
    avatar = '/static/logo.svg'  # надо брать у юзера

    class Meta:
        ordering = ('-rating',)
        verbose_name = u'ответ'
        verbose_name_plural = u'ответы'


class TagManager(models.Manager):
    def top(self):
        return self.all()[:5]


class Tag(models.Model):
    objects = TagManager()
    question = models.ManyToManyField(Question)
    tag = models.CharField(max_length=15)

    class Meta:
        verbose_name = u'тег'
        verbose_name_plural = u'теги'

    def __unicode__(self):
        return str(self.tag)

    def __str__(self):
        return str(self.tag)


class Profile(models.Model):
    user = models.OneToOneField(User)
    #    rating = models.IntegerField(default=0)
    avatar = models.CharField(max_length=40)

    class Meta:
        verbose_name = u'профиль'
        verbose_name_plural = u'профили'


class Like(models.Model):
    question = models.ForeignKey(Question, null=True, default=None)
    answer = models.ForeignKey(Answer, null=True, default=None)
    profile = models.ForeignKey(Profile)

    class Meta:
        verbose_name = u'лайк'
        verbose_name_plural = u'лайки'
