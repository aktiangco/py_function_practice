# Activity: Zoo
# *! To check: python3 day3/zoo.py

class Person:
  def __init__(self,in_name,in_age):
    self.name = in_name
    self.age = in_age
      
  def get_name(self):
    return self.name
  
'''
Next, let's try defining a class to represent a customer. A customer is a person, so the Customer class inherits from the Person class, and should call the Person constructor inside the Customer constructor. In addition to their name and age, a customer should have two Booleans, one each for whether they have a ticket for the zoo, and whether they are currently in the zoo. Initialize these Booleans to false in the constructor for your Customer class.
'''
class Customer(Person):
    def __init__(self, in_name, age):
        super().__init__(in_name, age)
        self.has_ticket = False
        self.in_zoo = False
        
    # * After you have defined your Customer class and written the constructor, add the following methods to your class:
    '''
    buy_ticket
      The Customer's hasTicket attribute should be set to true, and an appropriate message should be printed out. As a bonus, print a different message depending on whether an adult or child's ticket is purchased.
    '''         
    def buy_ticket(self):
        self.has_ticket = True
        if self.age <=12:
            print(f"{self.name} has purchased an adult ticket.")
        else:
            print(f"{self.name} has purchased a child ticket.")
    '''
    enter_zoo
      This method should accept the Zoo object of the zoo the customer is attempting to enter. If the Customer's hasTicket attribute is true, it is set to false, the Zoo's add_customer method is called, and the Customer's inZoo attribute is set to true. If the Customer's hasTicket attribute is false, print a message prompting the customer to purchase a ticket before attempting to enter the zoo.
    '''  
    def enter_zoo(self, zoo):
        if self.has_ticket:
            self.has_ticket = False
            zoo.add_customer(self)
            self.in_zoo = True
            print(f"{self.name} has entered the zoo.")
        else:
            print(f"{self.name} needs to purchase a ticket before entering the zoo.")
    '''
    exit_zoo
      Accepts the Zoo object of the zoo the customer is attempting to leave. If the Customer's inZoo attribute is true, set it to false and call the Zoo's remove_customer method.
    '''
    def exit_zoo(self, zoo):
        if self.in_zoo:
            self.in_zoo = False
            zoo.remove_customer(self)
            print(f"{self.name} has exited the zoo.")
        else:
            print(f"{self.name} is not currently in the zoo.")

  

class Zoo:
  def __init__(self,name="Local Zoo"):
    self.name = name
    self.animals = []
    self.customers = []

  def add_animal(self, animal):
    self.animals.append(animal)
    print(f"{self.name} has a(n) {animal}")
  
  def add_animals(self, animals):
    self.animals.extend(animals)
    print(f"{self.name} has many animals")
  
  def add_customer(self, name):
    self.customers.append(name)
    print(f"{name} has entered {self.name}")

  def remove_customer(self, name):
    self.customers.remove(name)
    print(f"{name} has left {self.name}")
  
  def visit_animals(self):
    for a in self.animals:
      print(f"visiting {a.get_name()}")
      a.make_noise()
      a.eat_food()

#* Now that your Customer class is complete, let's create some animal classes. Each subclass should call the Animal constructor in its own constructor and should override the make_noise and eat_food methods to print appropriate messages.
'''
Make sure to create at least three different Animal subclasses. We suggest Fish, Bird, and Chimp.
'''
class Animal:
  def __init__(self,name):
    self.name = name
  def get_name(self):
    return self.name
  def make_noise(self):
    print("Every animal makes noise")
  def eat_food(self):
    print("All creatures need sustenance")
    
class Fish(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_noise(self):
        print(f"{self.name}Glub glub")

    def eat_food(self):
        print(f"{self.name}Eating fish flakes")

class Bird(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_noise(self):
        print(f"{self.name}Tweet tweet")

    def eat_food(self):
        print(f"{self.name}Eating birdseed")

class Chimp(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_noise(self):
        print(f"{self.name}Ooh ooh aah aah")

    def eat_food(self):
        print(f"{self.name}Eating bananas")



nycZoo = Zoo("NYC Zoo")

salmon = Fish("salmon")
robin = Bird("robin")
bonobo = Chimp("bonobo")
nycZoo.add_animals([salmon, robin, bonobo])

alice = Customer("Alice",25)
bob = Customer("Bob",20)
charlie = Customer("Charlie",10)
dave = Customer("Dave",30)
for c in [alice, bob, charlie, dave]:
  c.buy_ticket()
  c.enter_zoo(nycZoo)
nycZoo.visit_animals()
for c in [alice, bob, charlie, dave]:
  c.exit_zoo(nycZoo)