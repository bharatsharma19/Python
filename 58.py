def searcher():
    import time
    # Some 4 seconds time consuming task
    book = "This is a book\n"
    time.sleep(4)

    while True:
        text = (yield)
        if text in book:
            print("Your text in the book\n")
        else:
            print("Text is not in the book\n")


search = searcher()
next(search)
search.send("Bharat")
input("Press Enter\n")
search.send("This")
search.close()
