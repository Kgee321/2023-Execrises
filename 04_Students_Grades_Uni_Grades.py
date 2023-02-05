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

    # Asking for student name and grade
    question = input("Student name and mark: ").split(" ")

# Dictionary is sorted by value
number_list = sorted(dic)

# highest value found
highest = number_list[-1]

# Outputting student with the highest grade
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
