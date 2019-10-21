class Dog:
    species = 'caniche'

    def __init__(self, name, age):
        self.name = name
        self.age = age


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