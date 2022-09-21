def snack_check(choice, options):

    for var_list in options:
        if choice in var_list:
            chosen = var_list[0].title()
            is_valid = "yes"
            break
        else:
            is_valid = "no"

    if is_valid == "yes":
        return chosen
    else:
        return "invalid choice"

Valid_snacks = [
    ["popcorn", "p", "corn", "a" ],
    ["M&M's", "m&m's", "mms", "m", "b"],
    ["pita chips", "chips", "pc", "pita", "c"],
    ["water", "w", "d"]
]

snack_ok = ""
snack = ""

for item in range(0, 3):
    desired_snack = input("Snack:  ").lower()
    snack_choice = snack_check(desired_snack, Valid_snacks)
    print("snack_choice: ", snack_choice)
