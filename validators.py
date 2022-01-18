def input_postal_code(prompt, *postalcodes):
    while True:
        value = input(prompt)

        if value == "q" or value == "Q":
            print("Choose again:")
            return None

        try:
            return _check_postalcode(value, postalcodes)
        except ValueError as error:
            print(error)


# def _concatenate(postalcodes):
# return ", ".join(str(code) for code in postalcodes)


def _check_postalcode(value, postalcodes):
    try:
        postalcode = int(value)
    except ValueError:
        raise ValueError("Please enter a valid postalcode:", postalcodes, "Your input", value, "is not numeric.")

    if postalcode not in postalcodes:
        raise ValueError("Your input", value, "is not part of the postal code list. Please try again.")

    return postalcode


def input_bounded_integer(prompt, description, minimum, maximum):
    while True:
        value = input(prompt)

        if value == "q" or value == "Q":
            print("Choose again:")
            return None

        try:
            return _check_bounded_integer(value, description, minimum, maximum)
        except ValueError as error:
            print(error)


def _check_bounded_integer(value, description, minimum, maximum):
    try:
        value = int(value)
    except ValueError:
        raise ValueError("Please enter a valid age/height:""(between", minimum, "and", maximum, "). Your input", value,
                         "is not numeric.")

    if value not in range(minimum-1, maximum+1):
        raise ValueError("Your input", value, "is not part of the valid integer list. Please try again.")

    return value
