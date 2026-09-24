Objective
In this assignment you will leverage inheritance and polymorphism to build a vehicle class hierarchy in Python. You will practice:

definition and implementation of abstract methods (using the abc module);
use of default parameters to achieve constructor-like overloading;
implementation of comparison dunder methods (__lt__, __eq__) to make vehicle objects sortable;
use of inheritance and polymorphism;
identifying common fields/methods across derived classes and pulling them into an abstract base class to improve reuse;
writing clean, well-documented, incremental commits in Git.
The class hierarchy you will build:

image.png

Supporting classes: Manufacturer, AutoModel, Garage.

Collaboration & Deliverables
Item	Details
Pair testing	You must pair up with another student. Your partner acts as a tester for your repository: they must clone your repo, run the instructor-provided unit tests, file at least two GitHub Issues (bugs, style, or suggestions), and you must address those issues with additional commits. You will do the same for their repo.
Incremental commits	Each small, logical change must be its own commit with a clear, descriptive message (e.g., "add Manufacturer class with __str__"). A submission with only one or two giant commits will lose points. Aim for at least 10 meaningful commits.
Deliverable	Submit the URL of your public GitHub repository. The repository must contain all .py source files described below, your partner's Issues (visible on GitHub), and your responses/commits addressing them. SCREENSHOT of all instructor test cases passing. 
Getting Started
Create a public GitHub repository named F26_IST242_ASG03_vehicles_<name>.
Clone it locally and create the project structure:
F26_IST242_ASG03_vehicles_<name>/
├── manufacturer.py
├── auto_model.py
├── vehicle.py
├── sedan.py
├── truck.py
├── garage.py
├── main.py # your main script
└── README.md # brief description, your name, partner's name
Make an initial commit with the empty files and README.md.
Part 1: Manufacturer and AutoModel
Manufacturer (manufacturer.py)
Create a Manufacturer class that stores:

name (str)
country (str)
Provide:

An __init__ that accepts both fields.
Use the single leading-underscore convention (self._name) for all instance attributes to signal they are non-public, and expose each through a @property getter.
A __str__ method that returns:
<name>, <country>
AutoModel (auto_model.py)
Create an AutoModel class that stores:

name (str) — the model name
in_production (bool) — whether the model is still in production
years (list of int) — the years the model was produced
Provide:

An __init__ that accepts all three fields. Include a defensive check: if the years list is empty, raise a ValueError with a descriptive message.
@property getters for each field.
A __str__ method that returns:
<model-name> in production = <whether-in-production>, release year: <first-year-in-list>
(Note: you no longer need to store or add trims.)

Commit your work so far with a clear message.

Part 2: Stubbing Out the Vehicle Hierarchy
Vehicle (vehicle.py)
Create an abstract class Vehicle using Python's abc module:

python
from abc import ABC, abstractmethod
Examine the Sedan and Truck classes below. Identify the common fields between them and store those fields in Vehicle. Create an __init__ that accepts the corresponding parameters (subclass constructors will call super().__init__(...)).

The Vehicle class must provide:

@property getters for each common field you identify.
A release_year property that returns the vehicle's first production year as an int (derived from the AutoModel's year list — do not pass the release year as a separate constructor parameter).
An abstract method number_of_wheels(self) → int.
A concrete method how_far_with(self, num_of_gallons: int) -> float that returns how many miles the vehicle can travel on the given number of gallons (based on mpg).
Sedan (sedan.py)
Sedan extends Vehicle and stores:

manufacturer (Manufacturer)
model (AutoModel)
mpg (float)
Determine which of these belong in Vehicle (hint: all of them are shared with Truck). Call super().__init__(...) with the appropriate arguments.

Implement number_of_wheels — always returns 4.

Override __str__ to return:

(<manufacturer>) <model>, mpg: <mpg formatted to 2 decimal places>
For example:

(Honda, Japan) Civic in production = False, release year: 1996, mpg: 28.00
Truck (truck.py)
Truck extends Vehicle and stores one additional field beyond what Vehicle already provides:

is_dually (bool)
Its __init__ must accept: manufacturer, model, mpg, and is_dually with a default value of False (this replaces Java-style constructor overloading). Call super().__init__(...).

Implement number_of_wheels: returns 6 if dually, 4 otherwise.

Override __str__:

(<manufacturer>) <model>, mpg: <mpg formatted to 2 decimal places> is dually truck: <is_dually>
Commit after completing each class.

Part 3: Making Vehicles Comparable
Make Vehicle sortable by release year by implementing the following dunder methods inside Vehicle:

Method	Return value
__eq__(self, other)	True if release years are equal
__lt__(self, other)	True if self.release_year < other.release_year
With __eq__ and __lt__ defined, Python's built-in sorted() and list.sort() will work correctly.

(Optional but encouraged: use @functools.total_ordering to get <=, >, >= for free.)

Commit this change.

Part 4: Garage Class and Main
Garage (garage.py)
The Garage class stores a single private field _vehicles (a Python list). Provide:

Method	Description
add_vehicle(vehicle)	Appends a Vehicle to the list. Returns None.
empty_garage()	Clears the list using the list's .clear() method (do not set the list to None). Returns None.
sort_by_release_year()	Sorts _vehicles in place (you may simply call self._vehicles.sort()).
__str__	Returns each vehicle on its own line.
Also provide a @property called vehicles that returns a copy of the internal list (to protect encapsulation).

Main (main.py)
Write a main.py script (with a if __name__ == "__main__": guard) that:

Creates the following vehicles (invent reasonable mpg values where needed):
Vehicle	Manufacturer	Model	Production Years	Extra
Ford F150 (Truck)	Ford, USA	F150	2020–2022	not dually, mpg 20
Honda Civic LX (Sedan)	Honda, Japan	Civic	1996–1998	mpg 28
BMW M3 Limited (Sedan)	BMW, Germany	M3 Limited	2015–2018	mpg 30
Toyota Tundra (Truck)	Toyota, Japan	Tundra	1987–1988	dually, mpg 30
Instantiates a Garage named g, adds all four vehicles.
Prints "Before sorting:" followed by g.
Calls g.sort_by_release_year().
Prints "After sorting:" followed by g.
Expected output:

Before sorting:
(Ford, USA) F150 in production = True,  release year: 2020, mpg: 20.00 is dually truck: False
(Honda, Japan) Civic in production = False,  release year: 1996, mpg: 28.00
(BMW, Germany) M3 Limited in production = False,  release year: 2015, mpg: 30.00
(Toyota, Japan) Tundra in production = False,  release year: 1987, mpg: 30.00 is dually truck: True

After sorting:
(Toyota, Japan) Tundra in production = False,  release year: 1987, mpg: 30.00 is dually truck: True
(Honda, Japan) Civic in production = False,  release year: 1996, mpg: 28.00
(BMW, Germany) M3 Limited in production = False,  release year: 2015, mpg: 30.00
(Ford, USA) F150 in production = True,  release year: 2020, mpg: 20.00 is dually truck: False
Commit your `main` and any final polishing.

Grading Rubric (100 pts)
Criterion	Points
Manufacturer class correct	5
AutoModel class correct (including ValueError check)	10
Vehicle abstract class (common fields, abstract method, how_far_with, comparison methods)	20
Sedan class correct	10
Truck class correct (including default parameter for is_dually)	10
Garage class correct	10
Main output matches expected	10
All instructor-provided unit tests pass	10
Incremental commits (≥ 10 meaningful commits with clear messages)	5
Testing: Issues filed and addressed	5
Code style & documentation	5
Submission
Submit your GitHub repository URL on Canvas by the due date. Make sure:

Your repository is public (or the instructor and your partner are added as collaborators).
All .py files are in the root of the repository.
Your partner has filed at least two Issues and you have addressed them.
Your README.md lists your name and your partner's name.
The instructor-provided unit test file passes when placed in your repository root and run with python -m pytest test_vehicles.py -v.
Upload a SCREENSHOT showing that all instructor test cases are indeed passing. 