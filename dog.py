class Dog:
    species = 'caniche'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Returns biggest numbers of passed ones.  
    def get_biggest_number(self, *args):
        if len(args) > 0 :
            biggest_number = args[0]
            # Iterate over all the arguments and calculate max
            for i in range(len(args)):
                if args[i] > biggest_number:
                    biggest_number = args[i]
        return biggest_number
    
    # Method for printing the class
    def __str__(self):
        return "{0} is a {1} of {2} years old!".format(
            dog.name, dog.species, dog.age)



bambi = Dog("Bambi", 5)
mikey = Dog("Rufus", 6)

print("{} is {} and {} is {}.".format(
    bambi.name, bambi.age, mikey.name, mikey.age))

# comparison is changed from "mammcanicheal" to "caniche"
if bambi.species == "caniche":
    print("{0} is a {1}!".format(bambi.name, bambi.species))

# the three instances are created
bluedog = Dog("Chase", 4)
reddog = Dog("Marshall", 7)
yellowdog = Dog("Rubble", 8)

# the instances are checked
dogs = [bluedog, reddog, yellowdog]
for dog in dogs:
    print("{0} is a {1} of {2} years old!".format(dog.name, dog.species, dog.age))

# now with the print method is used
for dog in dogs:
    print(dog)

# it is checked the get_biggest_number
# A single number
print("%d" % bambi.get_biggest_number(5))
# 5 numbers
print("%d" % bambi.get_biggest_number(5,9,20,4,8))
# 10 numbers
print("%d" % bambi.get_biggest_number(5,9,20,4,8,1,4,6,100,6))