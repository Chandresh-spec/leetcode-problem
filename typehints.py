class Person:
    def __init__(self, name):
        self.name = name


def print_name(person: Person):
    print(person.name)


print_name(Person("hello"))