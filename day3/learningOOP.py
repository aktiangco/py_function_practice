# Activity: Practice OOP Fundamentals
# *! To check: python3 day3/learningOOP.py

class Car:
  def __init__(self, name, max_speed):
    self.name = name
    self.max_speed = max_speed

  def start(self):
    print('Vroom!')

  def talk(self, driver):
    print(f'Hello, {driver}, I am {self.name}.')

my_car = Car('Kitt', 180)
my_other_car = Car('Speedy', 55)

my_car.talk('Michael')


class Race:
  def __init__(self, name, driver_limit):
    self.name = name
    self.driver_limit = driver_limit
    self.drivers = []
  
  def add_driver(self, driver):
      if len(self.drivers) < self.driver_limit:
          self.drivers.append(driver)
      else:
          print("Race is full, cannot add more drivers.")
  
  def get_average_ranking(self):
      total_ranking = 0
      for driver in self.drivers:
          total_ranking += driver.get_ranking()
      return total_ranking / len(self.drivers)

class Driver:
  number_of_drivers = 0  # initialize a class variable
  
  def __init__(self, name, age, ranking):
    self.name = name
    self.age = age
    self.ranking = ranking
    Driver.number_of_drivers += 1
    
  def get_ranking(self):  # define the get_ranking method
      return self.ranking 

# Testing Driver
my_driver = Driver('Dale Earnhardt', 29, 100)
print(my_driver.get_ranking())

# prints a returned value of "100"

# Testing Race
my_course = Race('Seattle 500', 4)
print(my_course.name, my_course.driver_limit, my_course.drivers)

# prints Seattle 500 4 []

# Creating drivers and adding to race
lewis_hamilton = Driver('Lewis Hamilton', 36, 83)
eliud_kipchoge = Driver('Eliud Kipchoge', 36, 95)
sebastian_vettel = Driver('Sebastian Vettel', 34, 76)
ayrton_senna = Driver('Ayrton Senna', 34, 99)

my_course.add_driver(lewis_hamilton)
my_course.add_driver(eliud_kipchoge)
my_course.add_driver(sebastian_vettel)
my_course.add_driver(ayrton_senna)

# Getting average ranking of drivers in race
print(my_course.get_average_ranking())