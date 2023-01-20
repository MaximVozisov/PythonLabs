# -*- coding: utf_8 -*-

import json
from animal import Animal
from mammal import Mammal
class Dog(Mammal):
    def __init__(self, name = "", age = 0, gender = "", viewDog = ""):
        super().__init__(name,age,gender,"Собака")
        self.viewDog = viewDog
    def __repr__(self): 
        return self.__str__()
    def __str__(self):
        return str(self.__dict__)


def DogSerialize(dog,path):
    with open(path,"w") as outfile:
        json.dump(dog.__dict__,outfile)
def DogDeserialize(pas):
    def Decode(obj):
        if "viewDog" in obj:
            return Dog(obj["name"],obj["age"],obj["gender"],obj["viewDog"])
    with open(pas) as json_file:
        J = json.load(json_file)
    return Decode(J) 