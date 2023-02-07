""" Sounds travels at 340 m/s. Times the number of seconds input by 340 to find the storm distance """

# Setting variables
SOUND_TRAVELS = 340

while True:
    try:
        # User inputs seconds between lightening and thunder
        seconds = float(input("Seconds between lightening and thunder: "))
        break

    except ValueError:
        print("Please enter an number! Try again")
        print()

# Calculating distance
distance = seconds * SOUND_TRAVELS

# Distance in km
km = distance / 1000

# Outputting distance
print()
print(f"The storm is {distance:.3f} meters away and {round(km, 3)} kms away")


