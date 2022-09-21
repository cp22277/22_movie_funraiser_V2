while True:
    try:
        age = int(input("How old are you?"))
        if  12 > age or age > 130:
            print("please put a valid age")
            pass
        else:
            print("Thank you")
            break
    except ValueError:
        print("Please use numbers for this part.")

