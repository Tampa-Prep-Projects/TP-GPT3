import requests
from django.http import JsonResponse


def handle_submit(files):
    '''
    sentiment_file = files.get('sentiment-file')
    examples_files = files.getlist('examples-dir')

    # debug code, you can delete if needed
    print("Got files!")

    print("------")

    print("Sentiment file: " + sentiment_file.name)
    print("Examples files:")

    print("------")

    print(f"Sentiment file: {sentiment_file.read()}")

    # print out all example file names
    for f in examples_files:

        print(f.name, "contents: ")

        # Mr. Quah: Here's some example code to read contents of a file if needed!
        # I figured I'd include it just to show that f is a file
        print(f.read())
        print(f)

    '''

    # Make a sample API request as a test to simulate an OpenAI call
    response = requests.get("https://catfact.ninja/fact")
    fact = response.json().get("fact")
    print(f"FACT: {fact}")

    # now that the request has completed, let's change the submit button
    # to say "view results" instead of "submit"!
    return fact


# This is kind of a hacky way to do things, but it is seemingly the ONLY way
def send_update():
    return JsonResponse({"text": text})
