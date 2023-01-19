# -*- coding: cp1251 -*-

import csv
import random
from MapAndReduce import MyMap, MyReduce
FILENAME: str = "DataSet.csv" # ���� � ������������ �������
OUTPUTFILE: str = "NewDataSet.csv" # ���� � ���������������� �������

def FillDataSet() -> list:
    breed: list = ["����", "������", "����������", "���-���", "�����", "��������"]
    name: list = ["����", "���", "�����", "������", "����", "����", "����", "�����"]
    country: list = ["(������)", "(�������)", "(������)", "(���)", "(�����)", "(����������)", "(������)"]
    Dogs = list()
    i: int = 0
    countDog: int = 40
    Dogs.append(["������", "�������"])
    while i < countDog:
        randomDog = breed[random.randint(0, len(breed) - 1)] + " " + name[random.randint(0, len(name) - 1)] + " " + country[random.randint(0, len(country) - 1)]
        Dogs.append([randomDog, random.randint(0,11)])
        i += 1
    return Dogs

def WriteInCSV(dataSet: list, fileName: str): # ������ ����� �� ������ 
    with open(fileName, 'w', newline="") as file:
        writer = csv.writer(file, delimiter=',');
        writer.writerows(dataSet)

def WriteInCSVFromDict(dataSet: list, fileName: str): #������ ����� �� �������
    with open(fileName, 'w', newline="") as file:
        columns = list(dataSet[0].keys())
        writer = csv.DictWriter(file, fieldnames=columns, delimiter=',');
        writer.writeheader()
        writer.writerows(dataSet)

def ReadFromCSV(fileName: str) -> list: # ������ �����
    with open(fileName, 'r', newline="") as file:
        reader = csv.DictReader(file)
        newListDict = list()
        for dict in reader:
            newListDict.append(dict)
    return newListDict

def SplitDog(originalDict: dict) -> dict: #���������� ������� ������� �� 3 �����
    newDict = dict()
    strs = originalDict["������"].split(' ')
    newDict["������"] = strs[0]
    newDict["���"] = strs[1]
    newDict["������"] = strs[2]
    newDict["�������"] = originalDict["�������"]
    return newDict


def GetSumAgeDog(originalDict: dict, originalDict2: dict) ->dict:
    newDict = dict()
    newDict["�������"] = int(originalDict["�������"]) + int(originalDict2["�������"])
    return newDict

WriteInCSV(FillDataSet(), FILENAME) # ���������� �������
# ������� 1: ���������� ������� ������ �� 3 ����� ������� � ������� map � ����� ���� csv
dataSet: list = ReadFromCSV(FILENAME)
newDataSet: list = MyMap(SplitDog, dataSet)
WriteInCSVFromDict(newDataSet, OUTPUTFILE)
# ������� 2: �������������� ������� ����� � ����� �� ������� �������� � ������� reduce
summ = MyReduce(GetSumAgeDog, dataSet)["�������"]
summ = summ / 40
print("������� ������� �����", summ)