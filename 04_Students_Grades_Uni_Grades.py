""" Take student name and mark. Output top students and average student """

# Create dictionary
dic = {}
dic2 = {}

# Asking for student name and grade
question = input("Student name and mark: ").split(" ")

while question[0].lower() != "x":

    # Making the grade an integer
    mark = int(question[1])

    # Adding name and mark to dictionary
    dic[mark] = question[0]

    # Uni grade finding from mark
    if mark > 90:
        grade = "A+"
    elif 84 < mark < 89:
        grade = "A"
    elif 79 < mark < 84:
        grade = "A-"
    elif 74 < mark < 79:
        grade = "B+"
    elif 69 < mark < 74:
        grade = "B"
    elif 74 < mark < 69:
        grade = "B-"
    elif 59 < mark < 64:
        grade = "C+"
    elif 54 < mark < 59:
        grade = "C"
    elif 49 < mark < 54:
        grade = "C-"
    elif 39 < mark < 49:
        grade = "D"
    elif 0 < mark < 39:
        grade = "E"

    # Adding grades to dictionary
    dic2[grade] = question[0]

    # Asking for student name and grade
    question = input("Student name and mark: ").split(" ")

# Dictionary is sorted by value
number_list = sorted(dic)

# highest value found
highest = number_list[-1]

# Outputting student with the highest grade
print()
print(f"The student who got the best mark was {dic[highest].title()} with a mark of {highest}.")

# Total sum of numbers
total = 0
for i in number_list:
    total += i

# Average of numbers found
average = total/len(number_list)

# Outputting average mark of students
print()
print(f"The average mark of all the students was {average}")

# Outputting all students with uni grade
print()
for keys, value in dic2.items():
    print(value.title() + ": " + keys)


