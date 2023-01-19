# -*- coding: cp1251 -*-

import json
from animal import Animal
from mammal import Mammal
class Cat(Mammal):
    def __init__(self, name = "", age = 0, gender = "", viewCat = ""):
        super().__init__(name,age,gender,"Кошка")
        self.viewCat = viewCat
    def __repr__(self): 
        return self.__str__()
    def __str__(self):
        return str(self.__dict__)

def CatSerialize(cat,path):
    with open(path,"w") as outfile:
        json.dump(cat.__dict__,outfile)
def CatDeserialize(pas):
    def Decode(obj):
        if "viewCat" in obj:
            return Cat(obj["name"],obj["age"],obj["gender"],obj["viewCat"])
    with open(pas) as json_file:
        J = json.load(json_file)
    return Decode(J) 