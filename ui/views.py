from django.shortcuts import render, redirect
# import handle_submit from form_submit.py
from .form_submit import handle_submit
from django.http import JsonResponse


def home(request):
    if not request.user.is_authenticated:
        return redirect('/auth')

    if request.method == "POST":
        print("Got form type", request.content_type)
        # handle the form submission
        api_result = handle_submit(request.FILES)
        return JsonResponse({"text": "Hello World!"})

    return render(request, 'home.html', {'title': 'Report Card Commenter'})
