""" Take student name and mark. Output top students and average student """

# Create dictionary
dic = {}


# Asking for student name and grade
question = input("Student name and mark: ").split(" ")

while question[0].lower() != "x":
    # Making the grade an integer
    mark = int(question[1])

    # Adding name and mark to dictionary
    dic[mark] = question[0]
    print(dic)

    # Asking for student name and grade
    question = input("Student name and mark: ").split(" ")

# Dictionary is sorted by value
number_list = sorted(dic)

# highest value found
highest = number_list[-1]

# Outputting student with the highest grade
print(f"The student who got the best mark was {dic[highest].title()} with a mark of {highest}.")

