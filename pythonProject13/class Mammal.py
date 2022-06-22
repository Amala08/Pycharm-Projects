class Mammal:


    def __init__(self):
        self.dogs = 4
        self.cat = 4
        self.human = 2
        self.dog_bark = "Woof"
        self.cat_sound = "Meow"
        self.human_sound = "Have a nice day"

    def legs(self):
        print(f"{self.dogs}")
        print(f"{self.cat}")
        print(f"{self.human}")

    def sound(self):
        print(f"{self.dog_bark}")
        print(f"{self.cat_sound}")
        print(f"{self.human_sound}")


class Dog(Mammal):

    def legs(self):
        return self.dogs

    def sound(self):
        return self.dog_bark


class Cat(Mammal):

    def legs(self):
        return self.cat

    def sound(self):
        return self.cat_sound

class Human(Mammal):

    def legs(self):
        return self.human

    def sound(self):
        return self.human_sound
object_dog = Dog()
object_cat = Cat()
amala = Human()
print(f"Dog has {object_dog.legs()} Legs")
print(f"Amala says {amala.sound()}")
