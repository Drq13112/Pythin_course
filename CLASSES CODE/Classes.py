<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Authors: David Redondo and Mariano Álvarez

Introduction to using classes, methods, inheritance, encapsulation, 
polymorphism and composition

"""

# First of all, we will start building a simple class. We are going to use
# the vehicle concept.
# In order for the class could be built a builder is required. This method is
# inseparable from the class. The builder isthe one  who will create the class.
# Through the builder we can define the stuff which the class will do fist when it's created.
# After the builder has been executed, we will be able to use the rest of the class's methods


from random import *

class Vehicle:

    # builder or constructor
    def __init__(self, name):
        print("Vehicle created, name:", name)

        # Assinging an attribute to the object. In this case we can give it a name.
        self.name = name

    # Now we can include some methods. The methods will represent the vehicle's functions
    # As we know, the vehicles can move and stop, so let's define them.

    def move(self, optional):
        if optional == True:
            print('moving')
        return 'moving'

    def stop(self, optional):
        if optional == True:
            print('stopping')
        return 'stopping'

    def GiveName(self, optional):
        if optional == True:
            print(self.name)
            
        return self.name


    # The destructor it's special method which let us to delete the object we have built.
    # It's a good practice to delete the objects which we know with centainty if they won't be used more time

        
    # The destructor is a special method which let us to delete the object we have built.
    # It's a good practice to delete the objects which we know with centainty if they won't be used more

    def __del__(self):
        print('Destructor called,', self.name, 'deleted.')
        print("")


Light_McQueen = Vehicle('Light McQueen')
Light_McQueen.move(True)
Light_McQueen.stop(True)
del Light_McQueen


# We have the class 'Vehicle', but there are plenty of
# vehicle types such as cars, trucks, boats, airplains.
# Let's define them, using the class vehicle as commun base.
# Using the inheritance, we won't need to write again all the vehicle's methods that
# have already been defined.

# Creating a child class:
class airplane(Vehicle):

    # Getting the attributes which define a car
    def __init__(self, name, wings, engines):

        self.engines = engines
        self.wings = wings

        # invoking the __init__ of the parent class
        Vehicle.__init__(self, name)

        # Other way to call it:
        # super()__init__(name)

    def flying_in_the_sky(self):

        # We can use the parent's methods in the child class as they were his own.
        # It's easy to notice that because he are using 'self' before the methods.
        # That indicates the method belongs to the class which store it
        print("")
        self.move(True)
        print('Fying in the sky...')
        self.stop(True)
        print("")


F14 = airplane('F14', 2, 2)

F14.flying_in_the_sky()

del F14


# In addtion we can overload the parent's methods. We will use the the parent's methods
# to create new child methods. We can see the power of inheritance and polymorphism.

# In addtion we can overload the parent's methods. We will use the the parent's methods 
# to create new child's methods. We can see the power of inheritance and polymorphism.


# Creating a child class:


class car(Vehicle):

    # Getting the attributes which define a car
    def __init__(self, name, wheels, seats):

        self.wheels = wheels
        self.seats = seats

        # invoking the __init__ of the parent class
        Vehicle.__init__(self, name)

        # Other way to calling:
        # super()__init__(name)

    # We are overloading the parent's methods using its methods here
    def stop(self):

        print(Vehicle.stop(self, False) + ' car ' + Vehicle.GiveName(self, False))

    def move(self):

        print(Vehicle.move(self, False) + ' car ' + Vehicle.GiveName(self, False))

    def Going_on_the_road(self):

        print("")
        self.move()
        print('Going on the road...')
        self.stop()
        print("")


McQueen = car('McQueen', 4, 2)

McQueen.Going_on_the_road()

del McQueen

# Demonstration of private members
# A class can store parameter and variables and they
# can be accessed by different ways.

# Creating a base class

class Base:
    def __init__(self):

        # Private member
        self.__b = 4

# Creating a derived class


class Derived(Base):
    def __init__(self):

        # Calling constructor of
        # Base class
        Base.__init__(self)

obj1 = Derived()

obj2 = Base()


try:
    # Calling private memeber
    print("Accessing private member of obj1: ", obj1.__b)
    pass

except AttributeError as Error:
    print(Error)
    
try:
    # Calling private memeber
    print("Accessing private member of obj2: ", obj2.__b)
    pass
except AttributeError as Error:
    print(Error)
    
    
class Puzzle:
    def __init__(self):
        
        # Notice we need two underscore to define a private attribute
        self.__number_pieces=randint(0, 40)
    
    def give_number_pieces(self):
        
        return self.__number_pieces
    
    def modify_number_pieces(self,number_pieces):
        
        if(number_pieces>2):
            self.__number_pieces=number_pieces
        else:
            self.__number_pieces=3
            
            
london_tower= Puzzle()

print(london_tower.give_number_pieces())

london_tower.modify_number_pieces(90)

print(london_tower.give_number_pieces())
   

# To end this little instroduction to OOP we will see how composition works
# We are going to link two different classes, but the main difference lie in one of them can use the other one, but not the other way around.
# For example, owr car can use the object engin, but the engine cannot use the car, so here we have a composition relationship.
# The car is composited with the engine.

# Let's create the engine class
class Engine:
    
    # Notice we haven't define the constructor. 
    # There is a default constructor even we couldn't see it.
    # This one is a simple constructor which let us build the class quickly
    
    def engine_working(self):
        print('Engine working')

# Now we'll build a new class which uses our engine
class Truck(Vehicle):
    
    def __init__(self,name,horses_power):
        
        self.horses_power=horses_power
        
        # invoking the __init__ of the parent class
        Vehicle.__init__(self, name)
        
        # Creating an engine object inside the Truck class
        # Notice we are writing 'self' before creating the object.
        # We must do it because the object belongs to the class.
        # Like an attribute.
        self.Engine_Truck = Engine()
        
    def move(self):
        
        self.Engine_Truck.engine_working()
        print("moving")
print("")        
Camion = Truck('Camion',200)
Camion.move()
del Camion
        
=======
# -*- coding: utf-8 -*-
"""
Authors: David Redondo and Mariano Álvarez

Introduction to using classes, methods, inheritance, encapsulation, 
polymorphism and composition

"""

# First of all, we will start building a simple class. We are going to use
# the vehicle concept.
# In order for the class could be built a builder is required. This method is
# inseparable from the class. The builder isthe one  who will create the class.
# Through the builder we can define the stuff which the class will do fist when it's created.
# After the builder has been executed, we will be able to use the rest of the class's methods


from random import *

class Vehicle:

    # builder or constructor
    def __init__(self, name):
        print("Vehicle created, name:", name)

        # Assinging an attribute to the object. In this case we can give it a name.
        self.name = name

    # Now we can include some methods. The methods will represent the vehicle's functions
    # As we know, the vehicles can move and stop, so let's define them.

    def move(self, optional):
        if optional == True:
            print('moving')
        return 'moving'

    def stop(self, optional):
        if optional == True:
            print('stopping')
        return 'stopping'

    def GiveName(self, optional):
        if optional == True:
            print(self.name)
            
        return self.name


    # The destructor it's special method which let us to delete the object we have built.
    # It's a good practice to delete the objects which we know with centainty if they won't be used more time

        
    # The destructor is a special method which let us to delete the object we have built.
    # It's a good practice to delete the objects which we know with centainty if they won't be used more

    def __del__(self):
        print('Destructor called,', self.name, 'deleted.')
        print("")


Light_McQueen = Vehicle('Light McQueen')
Light_McQueen.move(True)
Light_McQueen.stop(True)
del Light_McQueen


# We have the class 'Vehicle', but there are plenty of
# vehicle types such as cars, trucks, boats, airplains.
# Let's define them, using the class vehicle as commun base.
# Using the inheritance, we won't need to write again all the vehicle's methods that
# have already been defined.

# Creating a child class:
class airplane(Vehicle):

    # Getting the attributes which define a car
    def __init__(self, name, wings, engines):

        self.engines = engines
        self.wings = wings

        # invoking the __init__ of the parent class
        Vehicle.__init__(self, name)

        # Other way to call it:
        # super()__init__(name)

    def flying_in_the_sky(self):

        # We can use the parent's methods in the child class as they were his own.
        # It's easy to notice that because he are using 'self' before the methods.
        # That indicates the method belongs to the class which store it
        print("")
        self.move(True)
        print('Fying in the sky...')
        self.stop(True)
        print("")


F14 = airplane('F14', 2, 2)

F14.flying_in_the_sky()

del F14


# In addtion we can overload the parent's methods. We will use the the parent's methods
# to create new child methods. We can see the power of inheritance and polymorphism.

# In addtion we can overload the parent's methods. We will use the the parent's methods 
# to create new child's methods. We can see the power of inheritance and polymorphism.


# Creating a child class:


class car(Vehicle):

    # Getting the attributes which define a car
    def __init__(self, name, wheels, seats):

        self.wheels = wheels
        self.seats = seats

        # invoking the __init__ of the parent class
        Vehicle.__init__(self, name)

        # Other way to calling:
        # super()__init__(name)

    # We are overloading the parent's methods using its methods here
    def stop(self):

        print(Vehicle.stop(self, False) + ' car ' + Vehicle.GiveName(self, False))

    def move(self):

        print(Vehicle.move(self, False) + ' car ' + Vehicle.GiveName(self, False))

    def Going_on_the_road(self):

        print("")
        self.move()
        print('Going on the road...')
        self.stop()
        print("")


McQueen = car('McQueen', 4, 2)

McQueen.Going_on_the_road()

del McQueen

# Demonstration of private members
# A class can store parameter and variables and they
# can be accessed by different ways.

# Creating a base class

class Base:
    def __init__(self):

        # Private member
        self.__b = 4

# Creating a derived class


class Derived(Base):
    def __init__(self):

        # Calling constructor of
        # Base class
        Base.__init__(self)

obj1 = Derived()

obj2 = Base()


try:
    # Calling private memeber
    print("Accessing private member of obj1: ", obj1.__b)
    pass

except AttributeError as Error:
    print(Error)
    
try:
    # Calling private memeber
    print("Accessing private member of obj2: ", obj2.__b)
    pass
except AttributeError as Error:
    print(Error)
    
    
class Puzzle:
    def __init__(self):
        
        # Notice we need two underscore to define a private attribute
        self.__number_pieces=randint(0, 40)
    
    def give_number_pieces(self):
        
        return self.__number_pieces
    
    def modify_number_pieces(self,number_pieces):
        
        if(number_pieces>2):
            self.__number_pieces=number_pieces
        else:
            self.__number_pieces=3
            
            
london_tower= Puzzle()

print(london_tower.give_number_pieces())

london_tower.modify_number_pieces(90)

print(london_tower.give_number_pieces())
   

# To end this little instroduction to OOP we will see how composition works
# We are going to link two different classes, but the main difference lie in one of them can use the other one, but not the other way around.
# For example, owr car can use the object engin, but the engine cannot use the car, so here we have a composition relationship.
# The car is composited with the engine.

# Let's create the engine class
class Engine:
    
    # Notice we haven't define the constructor. 
    # There is a default constructor even we couldn't see it.
    # This one is a simple constructor which let us build the class quickly
    
    def engine_working(self):
        print('Engine working')

# Now we'll build a new class which uses our engine
class Truck(Vehicle):
    
    def __init__(self,name,horses_power):
        
        self.horses_power=horses_power
        
        # invoking the __init__ of the parent class
        Vehicle.__init__(self, name)
        
        # Creating an engine object inside the Truck class
        # Notice we are writing 'self' before creating the object.
        # We must do it because the object belongs to the class.
        # Like an attribute.
        self.Engine_Truck = Engine()
        
    def move(self):
        
        self.Engine_Truck.engine_working()
        print("moving")
print("")        
Camion = Truck('Camion',200)
Camion.move()
del Camion
        
>>>>>>> 94cc937c85286f9ae8e1f0ecb5cd73312d4a6149
