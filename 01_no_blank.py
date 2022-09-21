def no_blank(question):
    valid = False
    while not valid:
        response = input(question)
        while response != "":
            return response
        else:
            print("Don't leave this blank")
no_blank("name:")




