import validators
import csv
person = {"name":"","age":"","height":"","postal code":""}
#print(person.keys())
#person.values()
while True:
    choice = input("Please choose which aspect to edit: (a)ge, (h)eight, (n)ame, (p)ostal code (or enter 'q' to quit):")
    match choice.casefold():
        case "n" | "name":
            person["name"] = validators.input_string("Please enter your name (Enter 'q' to quit):")
        case "a" | "age":
            person["age"] = validators.input_bounded_integer("Please enter your age (Enter 'q' to quit): ", "age", 0, 130)
        case "h" | "height":
            person["height"] = validators.input_bounded_integer("Please enter your height (Enter 'q' to quit): ", "height", 20, 250)
        case "p" | "postal code" | "postalcode":
            person["postal code"] = validators.input_postal_code("Please enter your postal code (Enter 'q' to quit): ", 1010, 1020, 1030)
        case "q" | "quit":
            with open("people.csv", "w", newline="", encoding="UTF-8") as csvfile:
                writer = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
                writer.writerow(["name", "age", "height", "postal code"])
                writer.writerow([person["name"], person["age"], person["height"], person["postal code"]])
            print(csvfile.closed)
            quit(print("Closing application."))




