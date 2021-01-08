#%%
someList = [0,1,2,3,4,5,6,7,8,9]
#%%
def calculateMean(someList)
    """ THis function calulates mean values """
    numberOfElements = 0
    sumOfElements = 0
    for number in someList:
        sumOfElements = sumOfElements + number
        numberOfElements = numberOfElements + 1
    return sumOfElemetns/numberOfElements
# %%
class Animal()
    def __init__(self, animalType):
        self.animalType = animalType

    def printAnimalType(self):
        print(self.animalType)
# %%
class Mammal(Animal):
    def __init__(self, animalType):
        self.animalType = animalType
        self.warmBlooded = True
# %%
