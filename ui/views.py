from django.shortcuts import render, redirect
# import handle_submit from form_submit.py
from .form_submit import handle_submit
# Create your views here.


def home(request):
    if request.method == "POST":
        print("Got form type", request.content_type)
        handle_submit(request.POST, request.FILES)
        return redirect('/')

    return render(request, 'home.html', {'title': 'Report Card Commenter'})
