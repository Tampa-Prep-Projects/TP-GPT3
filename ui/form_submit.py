def handle_submit(files):
    sentiment_file = files.get('sentiment-file')
    examples_files = files.getlist('examples-dir')

    # debug code, you can delete if needed
    print("Got files!")

    print("------")

    print("Sentiment file: " + sentiment_file.name)
    print("Examples files:")

    print("------")

    # print out all example file names
    for f in examples_files:
        print(f.name, "contents: ")

        # Mr. Quah: Here's some example code to read contents of a file if needed!
        # I figured I'd include it just to show that f is a file
        for line in f:
            print(line.decode('utf-8'))
