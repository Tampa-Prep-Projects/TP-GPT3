completed_comments_loc = ""

# files are as follows: name, contents
# you can redo this easily! (You may want to)

sentiment_file = ["", ""]
examples_file = ["", ""]

local_sentiment_file_path = None
local_examples_file_path = None

# handle the form submission
# takes two params: (request.POST, request.FILES)
# POST is a dictionary of form data
# FILES is a dictionary of files
# This is the entry point of the file!


def handle_submit(request, files):
    global completed_comments_loc
    global sentiment_file
    global examples_file

    completed_comments_loc = request.get('file-path')
    raw_sent_file = files.get('sentiment-file')
    raw_ex_file = files.get('examples-file')

    sentiment_file[0] = raw_sent_file
    examples_file[0] = raw_ex_file

    try:
        for line in raw_sent_file:
            sentiment_file[1] += line.decode('utf-8')

    except Exception as e:
        print("Error in sentiment file:", e)

    try:
        for line in raw_ex_file:
            examples_file[1] += line.decode('utf-8')

    except Exception as e:
        print("Error in examples file:", e)

    # This function can be deleted safetly, it simply makes a copy of the files on the server.
    # In fact, you might want to delete it, because it will (in its current state) break the
    # program since it never deletes the local files.
    create_files_locally()

    # reset values! This is necessary so we don't retain form data
    # There might be an issue though, in that if two teachers use this at the same time,
    # the files will get mixed up. It would have to be within the same <1 second though.
    examples_file = ["", ""]
    sentiment_file = ["", ""]
    completed_comments_loc = ""


def create_files_locally():
    global local_sentiment_file_path
    global local_examples_file_path

    local_sentiment_file_path = open("sentiment_file.txt", "w")
    local_examples_file_path = open("examples_file.txt", "w")

    local_sentiment_file_path.write(sentiment_file[1])
    local_examples_file_path.write(examples_file[1])

    local_sentiment_file_path.close()
    local_examples_file_path.close()

    # Done! Our files are created.
    # Issue: What if two people use this at the same time?
    # We need to make sure that the files are somehow unique to each user.
