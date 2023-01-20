# -*- coding: utf_8 -*-

import json
from animal import Animal
class Mammal(Animal):
    def __init__(self, name = "",age = 0,gender = "", view = ""):
        super().__init__(name, age, gender)
        self.view = view
    def __repr__(self): # отображение объекта в режиме отладки
        return self.__str__()
    def __str__(self):
        return str(self.__dict__)

def MammalSerialize(mammal,path):
    with open(path,"w") as outfile:
        json.dump(mammal.__dict__,outfile)
def MammalDeserialize(pas):
    def Decode(obj):
        if "view" in obj:
            return Mammal(obj["name"],obj["age"],obj["gender"],obj["view"])
    with open(pas) as json_file:
        J = json.load(json_file)
    return Decode(J)
