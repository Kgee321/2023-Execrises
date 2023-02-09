""" Radius of a sphere is inputted and outputted is the spheres area and volume """

# Setting variables
PIE = 3.14159

while True:
    try:
        # User inputs radius
        radius = int(input("Radius: "))
        break
    except ValueError:
        print("Please enter an integer")

# Area
area = 4 * PIE * (radius * radius)

# Surface area
surface = 4/3 * PIE * (radius * radius * radius)

# Output the area and surface area
print(f"The Area is {area:.2f} and the Surface Area {surface:.2f}")



