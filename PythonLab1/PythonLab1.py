# -*- coding: utf_8 -*-

import json
from pprint import pprint
from animal import Animal, AnimalSerialize, AnimalDeserialize
from mammal import Mammal, MammalSerialize, MammalDeserialize
from dog import Dog, DogSerialize, DogDeserialize
from cat import * #������������� ��

newAnimal = Animal("�������",7,"�")
newMammal = Mammal("���", 4, "�", "��������")
newDog = Dog("�����",7,"�","������")
newCat = Cat("�����",10,"�","�����")
print(newAnimal)
print(newMammal)
print(newDog)
print(newCat)
#������������/�������������� Animal
AnimalSerialize(newAnimal,"primer.json")
newAnimal2 = AnimalDeserialize("primer.json")
pprint(newAnimal2.__dict__)
#������������/�������������� Mammal
MammalSerialize(newMammal,"primer2.json")
newMammal2 = MammalDeserialize("primer2.json")
pprint(newMammal2.__dict__)
#������������/�������������� Dog
DogSerialize(newDog,"primer3.json")
newDog2 = DogDeserialize("primer3.json")
pprint(newDog2.__dict__)
#������������/�������������� Cat
CatSerialize(newCat,"primer.json")
newCat2 = CatDeserialize("primer.json")
pprint(newCat2.__dict__)