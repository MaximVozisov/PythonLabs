# -*- coding: cp1251 -*-

import csv
import random
from MapAndReduce import MyMap, MyReduce
FILENAME: str = "DataSet.csv" # файл с изначальными данными
OUTPUTFILE: str = "NewDataSet.csv" # файл с преобразованными данными

def FillDataSet() -> list:
    breed: list = ["Мопс", "Пудель", "Долматинец", "Чау-чау", "Бигль", "Доберман"]
    name: list = ["Олег", "Лео", "Барни", "Тайсон", "Локи", "Нора", "Рекс", "Рокки"]
    country: list = ["(Россия)", "(Франция)", "(Англия)", "(США)", "(Китай)", "(Нидерланды)", "(Швеция)"]
    Dogs = list()
    i: int = 0
    countDog: int = 40
    Dogs.append(["Собака", "Возраст"])
    while i < countDog:
        randomDog = breed[random.randint(0, len(breed) - 1)] + " " + name[random.randint(0, len(name) - 1)] + " " + country[random.randint(0, len(country) - 1)]
        Dogs.append([randomDog, random.randint(0,11)])
        i += 1
    return Dogs

def WriteInCSV(dataSet: list, fileName: str): # Запись файла из списка 
    with open(fileName, 'w', newline="") as file:
        writer = csv.writer(file, delimiter=',');
        writer.writerows(dataSet)

def WriteInCSVFromDict(dataSet: list, fileName: str): #Запись файла из словаря
    with open(fileName, 'w', newline="") as file:
        columns = list(dataSet[0].keys())
        writer = csv.DictWriter(file, fieldnames=columns, delimiter=',');
        writer.writeheader()
        writer.writerows(dataSet)

def ReadFromCSV(fileName: str) -> list: # Чтение файла
    with open(fileName, 'r', newline="") as file:
        reader = csv.DictReader(file)
        newListDict = list()
        for dict in reader:
            newListDict.append(dict)
    return newListDict

def SplitDog(originalDict: dict) -> dict: #Разделение первого столбца на 3 новых
    newDict = dict()
    strs = originalDict["Собака"].split(' ')
    newDict["Порода"] = strs[0]
    newDict["Имя"] = strs[1]
    newDict["Родина"] = strs[2]
    newDict["Возраст"] = originalDict["Возраст"]
    return newDict


def GetSumAgeDog(originalDict: dict, originalDict2: dict) ->dict:
    newDict = dict()
    newDict["Возраст"] = int(originalDict["Возраст"]) + int(originalDict2["Возраст"])
    return newDict

WriteInCSV(FillDataSet(), FILENAME) # заполнение таблицы
# Задание 1: Разделение столбца Собака на 3 новых столбца с помощью map в новый файл csv
dataSet: list = ReadFromCSV(FILENAME)
newDataSet: list = MyMap(SplitDog, dataSet)
WriteInCSVFromDict(newDataSet, OUTPUTFILE)
# Задание 2: Просуммировать возраст собак и найти их среднее значение с помощью reduce
summ = MyReduce(GetSumAgeDog, dataSet)["Возраст"]
summ = summ / 40
print("Средний возраст собак", summ)