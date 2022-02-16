import imp
from django.http import HttpResponse
from django.shortcuts import render
from .models import Comment, Document, Protein,Notification
from .fomrs import DocumentForm,ProteinForm,CommentForm,NotificationForm
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request,'index.html')


def doc_method(request):
    if request.method == 'POST':
        dataform = DocumentForm(request.POST)

        if dataform.is_valid():
            dataform.save()

    custom_form={
        'df':DocumentForm,
        'docs':Document.objects.all(),
    }
    return render(request,'document.html',custom_form)


def pro_method(request):
    if request.method == 'POST':
        dataform = ProteinForm(request.POST)

        if dataform.is_valid():
            dataform.save()

    custom_form={
        'pf':ProteinForm,
        'pros':Protein.objects.all(),
    }
    return render(request,'protein.html',custom_form)


def com_method(request):
    if request.method == 'POST':
        dataform = CommentForm(request.POST)

        if dataform.is_valid():
            dataform.save()


    custom_form={
        'cf':CommentForm,
        'coms':Comment.objects.all(),
    }
    return render(request,'comment.html',custom_form)


def noti_method(request):
    if request.method == 'POST':
        dataform = NotificationForm(request.POST)

        if dataform.is_valid():
            dataform.save()

    custom_form={
        'nf':NotificationForm,
        'notis':Notification.objects.all(),
    }
    return render(request,'noti.html',custom_form)