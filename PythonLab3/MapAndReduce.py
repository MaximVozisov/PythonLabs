# -*- coding: utf_8 -*-

def MyMap(func, originalList: list) -> list: #Реализация Map
    newList = list()
    for object in originalList:
        newList.append(func(object))
    return newList

def MyReduce(func, originalList: list): #Реализация Reduce
    i: int = 2
    length: int = len(originalList)
    result = func(originalList[0], originalList[1])
    while (i < length):
        result = func(result, originalList[i])
        i += 1
    return result