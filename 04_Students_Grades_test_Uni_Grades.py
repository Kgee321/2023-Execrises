""" Take student name and mark. Output top students and average student """

# Create lists
students = []
grades = []
uni = []

# Asking for student name and grade
question = input("Student name and mark: ").split(" ")

while question[0].lower() != "x":

    # Separating inputs
    name = question[0]
    mark = int(question[1])

    # Adding input to lists
    students.append(name)
    grades.append(mark)

    # Asking question again
    question = input("Student name and mark: ").split(" ")

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

    uni.append(grade)

# Creating variables
highest = 0
num_list = []
count = 0

# Finding highest grade
for num in grades:
    if num > highest:
        highest = num
        num_list.append(count)
    count += 1

# Finding the index of the highest grade
index = num_list[-1]

# Outputting the student with the highest grade
print()
print(f"The student who got the best mark was {students[index].title()} with a mark of {highest}.")

# Average find
average = sum(grades)/len(grades)

# Outputting average mark of students
print()
print(f"The average mark of all the students was {average}")

# Outputting students and their uni grade
print()
for i in range(len(students)):
    print(uni[i-1], students[i-1])



