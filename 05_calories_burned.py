""" Calculate calories burned for biking, swimming and jogging then calculates the amount of weight lost """

# Setting variables -- calories burned to the activities
BIKE = 200
JOG = 475
SWIM = 275
dic = {}
calories = []

while True:
    # User inputs activity and their hours
    activity_hours = input("Activity and Hours: ").split(" ")

    # Loop breaks when user inputs x
    while activity_hours[0].lower() != "x":

        # Separating activity and hours
        act = activity_hours[0].lower()
        hours = activity_hours[1]

        # Adding calories based on activity
        if act == "bike":
            calories.append(BIKE)
        elif act == "jog":
            calories.append(JOG)
        elif act == "swim":
            calories.append(SWIM)
        else:
            print("Not the right input. Please enter Bike, Jog or Swim")
            break

    # User inputs activity and their hours
    activity_hours = input("Activity and Hours: ").split(" ")

# Testing
print(calories)






