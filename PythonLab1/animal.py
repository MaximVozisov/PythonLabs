# -*- coding: cp1251 -*-

import json
class Animal:
    def __init__(self, name = "", age = 0, gender = ""):
        self.name = name
        self.age = age
        self.gender = gender
    def __repr__(self): # отображение объекта в режиме отладки
        return self.__str__()
    def __str__(self):
        return str(self.__dict__)
    

def AnimalSerialize(animal,path): #Сериализация
    with open(path,"w") as outfile:
        json.dump(animal.__dict__,outfile)
def AnimalDeserialize(pas): #Десериализация
    def Decode(obj):
        if "name" in obj:
            return Animal(obj["name"],obj["age"],obj["gender"])
    with open(pas) as json_file:
        J = json.load(json_file)
    return Decode(J)