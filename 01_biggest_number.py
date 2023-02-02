"""Input two numbers and output the higher value or message saying they are equal"""

number1 = int(input("First number: "))
number2 = int(input("Second number: "))

while number2 != 0 or number1 != 0:
    if number1 > number2:
        print(number1)
    elif number2 > number1:
        print(number2)
    elif number2 == number1:
        print("They are equal")
    number1 = int(input("First number: "))
    number2 = int(input("Second number: "))
