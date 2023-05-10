height = int(input("Please provide your height: "))
kids_height_requirement = 60
family_height_requirement = 120
white_knuckle_height_requirement = 180

if height >= 180:
    print("You can use all rides.")
elif height >= 120:
    print("You can use the kids & family rides.")
elif height >= 60:
    print("You can only use the kids rides.")
else:
    print("You're not high enough to use any rides.")