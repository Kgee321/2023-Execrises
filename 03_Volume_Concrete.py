""" Volume of concrete needed of each job and total needed for all jobs on a day
Foundation = 50
residential = 25"""



while True:
    build_type = input("Build type Residential or Commercial: ")
    build = build_type.lower()

    base = int(input("Base in Metres: "))
    height = int(input("Height in Metres: "))


    while build != "x":
        if build == "r":
            thick = 0.25
        elif build == "c":
            thick = 0.5
        else:
            break

        volume = base * height * thick
        print("Volume:", volume)
        build_type = input("Build type Residential or Commercial: ")
        build = build_type.lower()
        base = int(input("Base in Metres: "))
        height = int(input("Height in Metres: "))
