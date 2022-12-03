import os


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

    # open a file to write to
    testPath = os.getcwd() + "/ui/test.end"
    f = open(testPath, "r")
    contents = f.read()
    f.close()
    # os.remove(testPath)

    return contents
