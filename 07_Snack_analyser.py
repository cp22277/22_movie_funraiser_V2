import re


test_strings=[
    "popcorn",
    "2 pc",
    "1,50J",
    "40J",
]

for item in test_strings:
    number_regex = "^[1-9]"

    if re.match(number_regex, item):
        amount = int(item[0])
        desired_snack = item[1:]

    else:
        amount = 1
        desired_snack = item

    desired_snack = desired_snack.strip()

    print("amount:", amount)
    print("snack: ", desired_snack)
    print("length of snack:", len(desired_snack))

def string_check (choice, options):

number_regex = "^[1-9]"

valid_snacks = [
    ["popcorn", "p", "corn", "a"],
    ["M&M's", "m&m's", "mms", "m", "b"],
    ["pita chips", "chips", "pc", "pita", "c"],
    ["water", "w", "d"],
    ["orange juice", "oj", "o", "juice", "e"]
]

yes_no = [
    ["yes", "y"],
    ["No", "n"]
]
snack_order = []

check_snack = ""
while check_snack == "invalid choice":
    want_snack = input("Do you want to order snacks? ").lower()
    check_snack = (string_check(want_snack, yes_no))

if check_snack == "yes":

    desired_snack = ""
    while desired_snack != "xxx":

        snack_row = []

        desired_snack = input("Snack: ").lower()

        if desired_snack == "xxx":
            break

        if re.match(number_regex, desired_snack):
            amount = int(desired_snack[0])
            desired_snack = desired_snack[1:]

        else:
            amount = 1
            desired_snack = desired_snack

        desired_snack = desired_snack.strip()

        snack_choice = (string_check(desired_snack, valid_snacks))

        if amount >=5:
            print("sorry - we have a four snack maximum")
            snack_choice = "invalid choice"

            snack_row.append(amount)
            snack_row.append(snack_choice)


        if snack_choice != "xxx" and snack_choice != "invalid choice":
            snack_order.append("snack_row")

print()
if len(snack_order) == 0:
    print("Snacks Ordered: none")

else:
    print("Snacks Ordered:")

    for item in snack_order:
        print(item)

    print(snack_order)


