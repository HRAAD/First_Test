class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)
    
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

  def __str__(self):
    return f"{self.firstname} {self.lastname} {self.graduationyear}"

x = Student("Hussein", "Raad", 2022)
#Use the Person class to create an object, and then execute the printname method:

#x = Student("John", "Doe")
#x.printname()
print(x.firstname)
print(x.lastname)
print(x.graduationyear)
x.welcome()
print(x)
