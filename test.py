def snack_check(choice, options):

    for var_list in options:

        if choice in var_list:
            chosen = var_list[0] .title()
            is_valid = "yes"
            break

        else:
            is_valid = "no"

        if is_valid == "yes":
            return "chosen"
        else:
            return "invalid choice"
