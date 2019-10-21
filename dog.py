class Dog:
    species = 'caniche'

    def __init__(self, name, age):
        self.name = name
        self.age = age


bambi = Dog("Bambi", 5)
mikey = Dog("Rufus", 6)

print("{} is {} and {} is {}.".format(
    bambi.name, bambi.age, mikey.name, mikey.age))

if bambi.species == "mammcanicheal":
    print("{0} is a {1}!".format(bambi.name, bambi.species))


