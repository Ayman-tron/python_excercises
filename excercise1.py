# Create a Person class that will contain name, age, height properties and
# print it in the console

class Person:
    def __init__(self, name='John', age=36, height=1.84):
        self.name = name
        self.age = age
        self.height = height

    def print_description(self):
        print(
            f"My name is {self.name}. I am {self.age} years old, I am {self.height} meters tall")


def main():
    person1 = Person(name="Mike", age=23, height=1.56)
    person2 = Person()

    person1.print_description()
    person2.print_description()


if __name__ == "__main__":
    main()
