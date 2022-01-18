import validators

while True:
    choice = input("Please choose which aspect to edit: (a)ge, (h)eight, (p)ostal code (or enter 'q' to quit):")
    match choice.casefold():
        case "p" | "postal code" | "postalcode":
            print(validators.input_postal_code("Please enter your postal code (Enter 'q' to quit): ", 1010, 1020, 1030))
        case "a" | "age":
            print(validators.input_bounded_integer("Please enter your age (Enter 'q' to quit): ", "age", 0, 130))
        case "h" | "height":
            print(validators.input_bounded_integer("Please enter your height (Enter 'q' to quit): ", "height", 20, 250))
        case "q" | "quit":
            quit(print("Closing application."))




