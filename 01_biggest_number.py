"""Input two numbers and output the higher value or message saying they are equal"""


# Error check for first number
def error_check(position):

    # Error loop when int not entered
    while True:
        try:

            # Asking user to input both numbers
            number = int(input(f"{position} number: "))
            break

        except ValueError:

            # Wrong input so question redone
            print("Wrong input, please enter an integer")
            print()

    # Returning number
    return number


# Setting functions to values
number1 = error_check("first")
number2 = error_check("second")

# Loop cuts when 0 entered
while number1 != 0 or number2 != 0:

    # If number 1 higher
    if number1 > number2:
        print()
        print(f"The higher number is: {number1}")

    # If number 2 higher
    elif number2 > number1:
        print()
        print(f"The higher number is: {number2}")

    # If numbers equal
    elif number2 == number1:
        print()
        print("They are equal")

    # Setting functions to values
    print()
    number1 = error_check("first")
    number2 = error_check("second")

print("Goodbye!")
