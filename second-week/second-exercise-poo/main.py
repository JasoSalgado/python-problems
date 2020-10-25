class Person():
    def __init__(self, dni, name = "", age = 0, gender = "", weight = 0, height = 0):
        self.__dni = dni
        self.__name = name
        self.__age = age
        self.__gender = gender
        self.__weight = weight
        self.__height = height
    
    
    @property
    def gender(self):
        return self.gender
    

    @gender.setter
    def gender(self, gender):
        if gender == 'M':
            return True
        else: 
            return False
    
    
    def is_legal_age(self):
        if self.__age >= str(18):
            return True
        else:
            return False
    

    def check_gender(self):
        if self.gender != 'M':
            print("You entered 'W'. \n")
        else:
            print("Gender continues being 'M'. \n")
    

    def to_string(self):
        print(f"dni: {self.__dni}, \n age: {self.__age}, \n gender: {self.__gender}, \n weight: {self.__weight}, \n height: {self.__height}")


class Executable(Person):
    print(" ***** Enter the following data, please. *****")

    dni = input("Enter your dni: \n")
    name = input("Enter your name: \n")
    age = input("Enter your age: \n")
    gender = input("Enter your gender: \n")
    weight = input("Enter your weight: \n")
    height = input("Enter your height: \n")

    first_person = Person(dni, name, age, gender, weight, height)
    first_person.is_legal_age()
    print("\n ***** These are your data: ***** \n")
    first_person.to_string()