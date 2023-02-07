""" Take student name and mark. Output top students and average student """

# Create lists
students = []
grades = []

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

# outputting the student with highest grade
print(f"The student who got the best mark was {students[index].title()} with a mark of {highest}.")




