"""
EXERCISES
Exercise 1
- Write a Python class which has two methods get_String and print_String. get_String accept a string from the user and
print_String print the string in upper case.
"""

# My example 1

class Python_String:

    def get_string(self, func):
        self.user_string = input("Enter some input ")
        return self.user_string

    def print_string(self):
        self.get_string(self)
        print(self.user_string.upper())

string = Python_String()
string.print_string()

# My example 2

class Python_String:

    def get_string(self):
        self.user_string = input("Enter some input ")
        return self.user_string

    def print_string(self):
        Python_String.get_string(self)
        print(self.user_string.upper())

string = Python_String()
string.print_string()

# Claire's example

class String_1():

    def get_String(self):
        self.string = input ('Give me a string: ')

    def print_String(self):
        print(self.string.upper())
s = String_1()

s.get_String()
s.print_String()

'''
Exercise 2
- Create a Python class Person with attributes: name and age of type string.
- Create a display() method that displays the name and age of an object created via the Person class.
- Create a child class Student  which inherits from the Person class and which also has a section attribute.
- Create a method displayStudent() that displays the name, age and section of an object created via the Student class.
- Create a student object via an instantiation on the Student class and then test the displayStudent method
'''

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name: {}, age: {}".format(self.name, self.age))

p1 = Person("Nasian", 23)
p1.display()

class Student(Person):

    def __init__(self, name, age, section):
        # when using the super method remember to call it on the init method with the arguments that you wan to
        # inherit from the parent class
        super().__init__(name, age)
        self.section = section

    def displayStudent(self):
        print("Name: {}, Age: {} and Section: {}.".format(self.name, self.age, self.section))

s1 = Student("Nasian", 23, 'Physics')
s1.displayStudent()


# Solution from Andreea

class Person:
    # define constructor with name and age as parameters
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # create display method fro Person class
    def display(self):
        print("Person name : ", self.name)
        print("Person age = ", self.age)

# FINISH OF THE TEST TOMORROW

# create child class Student of Person class
class Student(Person):
    # define constructor of Student class with section additional parameters
    def __init__(self, name, age, section):
        # super().__init__(name, age)
        # OR
        Person.__init__(self, name, age)
        self.section = section

    # Create display method for Student class
    def displayStudent(self):
        print("Student name : ", self.name)
        print("Student age = ", self.age)
        print("Student section = ", self.section)


# Testing Person class
P = Person("Tomas Wild", 37)
P.display()
print("-------------------------------")
S = Student("Albert", 23, "Mathematics")
S.displayStudent()
