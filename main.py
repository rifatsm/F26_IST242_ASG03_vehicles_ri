"""
The main entry point for ASG03 Vehicle Hierarchy with ABC

Author: Mr. Ri
"""

from manufacturer import Manufacturer

def main():

    """
    (Ford, USA)` F150 in production = True,  release year: 2020, mpg: 20.00 is dually truck: False
    (Honda, Japan) Civic in production = False,  release year: 1996, mpg: 28.00
    (BMW, Germany) M3 Limited in production = False,  release year: 2015, mpg: 30.00
    (Toyota, Ja`pan) Tundra in production = False,  release year: 1987, mpg: 30.00 is dually truck: True
    """
    ford = Manufacturer("Ford", "USA")
    honda = Manufacturer("Honda", "Japan")
    bmw = Manufacturer("BMW", "Germany")
    toyota = Manufacturer("Toyota", "Japan")

    print(ford) # printing the object location :/ 

if __name__ == "__main__":
    main()