class Student:
    def __init__ (self):
        self.__name=""
        self.__rno=""
    def setName(self):
         self.__name=input("Enter the name")
    def getName(self):
        return self.__name
    def setRollNumber(self):
         self.__rno=input("Enter the roll no")
    def getRollNumber(self):
        return self.__rno
obj=Student()
obj.setName()
print(obj.getName())
obj.setRollNumber()
print(obj.getRollNumber())