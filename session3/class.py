class Person:
    def __init__(self, name, age):
        self.name = name
        person_age = age

    def introduce(self):
        print("name {name} with age {age}".format(self.name, person_age))
