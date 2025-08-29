class Animal:
    def move(self):
        raise NotImplementedError("Subclass must implement this method")

class Dog(Animal):
    def move(self):
        print("🐕 Running on 4 legs")

class Bird(Animal):
    def move(self):
        print("🐦 Flying in the sky")

class Fish(Animal):
    def move(self):
        print("🐟 Swimming in water")

# Polymorphism in action
animals = [Dog(), Bird(), Fish()]

for animal in animals:
    animal.move()  # Each responds differently
