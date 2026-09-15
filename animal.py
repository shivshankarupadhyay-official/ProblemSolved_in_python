class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def sound(self):
        print(self.name, "says: Woof!")


class Cat(Animal):
    def sound(self):
        print(self.name, "says: Meow!")


d = Dog("Tommy")
c = Cat("Kitty")

d.sound()
c.sound()