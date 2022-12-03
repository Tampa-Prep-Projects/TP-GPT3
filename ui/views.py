from django.shortcuts import render, redirect, HttpResponse
# import handle_submit from form_submit.py
from .form_submit import handle_submit
import time


def home(request):
    if not request.user.is_authenticated:
        return redirect('/auth')

    if request.method == "POST":
        print("Got form type", request.content_type)
        # handle the form submission
        api_result = handle_submit(request.FILES)
        return render(request, 'result.html', {'file_contents': api_result})

    return render(request, 'home.html', {'title': 'Report Card Commenter'})
