height = int(input("Please provide your height: "))
park = input("Park choice: parkA, parkB, parkC. \n")
kids_height_requirement = 60
family_height_requirement = 120
white_knuckle_height_requirement = 180
permited_parks = ["parkA", "parkB", "parkC"]

if height >= white_knuckle_height_requirement and park >= permited_parks[0]:
    print("You can use all rides.")
elif height >= family_height_requirement and  park >= permited_parks[1]:
    print("You can use the kids & family rides.")
elif height >= kids_height_requirement and park >= permited_parks[2]:
    print("You can only use the kids rides.")
else:
    print("You're not high enough to use any rides. Or chosen park is not in our permited list")