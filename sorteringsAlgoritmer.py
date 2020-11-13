import random, math, sys


def InsertionSort(items):
    for i in range(1, len(items)):
        j = i
        while j > 0 and items[j-1] > items[j]:
            items[j-1], items[j] = items[j], items[j-1]
            j = j-1
    return items

usortert = [12,56,7785,342,7]
print('usortert')
print(usortert)
print('Insertion')
print(InsertionSort(usortert))

def bubbleSort(items):
    for index in range(len(items)-1,0,-1):
        for i in range(index):
            if items[i]>items[i+1]:
                temp = items[i]
                items[i] = items[i+1]
                items[i+1] = temp
    return items
usortert = [12,56,7785,342,7]

print('usortert')
print(usortert)
print('bubble')
print(bubbleSort(usortert))
