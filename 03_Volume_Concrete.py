""" Volume of concrete needed of each job and total needed for all jobs on a day
Foundation = 50
residential = 25"""

# Creating empty list
total_volumes = []

# loop if wrong build type inputted
while True:

    # Asking for build type input
    build_type = input("Build type - Residential (R) or Commercial (C): ")
    build = build_type.lower()

    # Loop so program ends when x entered
    while build != "x":

        # Setting thick to either 0.25 or 0.5 if user entered R or C
        if build == "r":
            thick = 0.25
        elif build == "c":
            thick = 0.5

        # Breaking the loop is R or C or X is not the input
        else:
            print("That is not a correct building type. Please enter R or C")
            break

        # Asking for measurements
        base = int(input("Base in Metres: "))
        height = int(input("Height in Metres: "))

        # Calculating the volume of the 1 concrete slab and outputing results
        volume = base * height * thick
        print(f"The volume of concrete required for a slab with a "
              f"length of {base} and a width of {height} and a depth "
              f"of {thick} is {volume} cubic metres.")

        # Adding volume to list
        total_volumes.append(volume)

        # Asking questions to keep loop going
        print()
        build_type = input("Build type Residential or Commercial: ")
        build = build_type.lower()

    # Breaking the bug loop when x inputted
    if build == "x":
        break

# Creating variables
sum_volumes = 0

# Adding the total volumes in list together
for i in total_volumes:
    sum_volumes += i

# Outputting final volumes sum results
print(f"The total concrete needed today is {sum_volumes} cubic metres")
