#!/usr/bin/env python3

class Dog:
    def __init__(self, name, breed = "Mutt"):
        pass
        self.name = name
        self.breed = breed

puff = Dog("puff", "Beagle")
print(puff.breed)