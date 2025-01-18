
# Vacation Booking System

## Overview

This Python script implements a **Vacation Booking System** using dictionaries to simulate classes and inheritance. The system defines different types of vacation packages (Beach Resort, Adventure Trip, and Luxury Cruise) and provides methods to calculate the cost and describe the package based on the specific type of vacation. 

## Part 1 Documentation

## Design Decisions

### Use of Dictionaries

The system is built entirely using Python dictionaries, representing the parent class `VacationPackage` and its subclasses `BeachResort`, `AdventureTrip`, and `LuxuryCruise`. Each dictionary contains attributes and methods relevant to the respective class, and inheritance is simulated by having a `_parent` key in each subclass.

### `make` Function

The `make` function works as a constructor for the vacation package objects. It accepts the class type and arguments, invoking the `_new` method for object instantiation.

### Inheritance and Method Lookup

The `find` function is used to implement inheritance. It searches for a method in the current class dictionary, and if not found, it recursively checks the parent class.

### The `call` function
The `call` function executes a method of a class instance based on the method name and instance name.

### Vacation Types

- **VacationPackage (Parent Class):** This is the base class, defining common attributes such as `destination`, `cost_per_day`, and `duration_in_days`. It also includes abstract methods `calculate_cost` and `describe_package`, which are overridden by subclasses.

- **BeachResort (Child Class):** Inherits from `VacationPackage` with an additional attribute `includes_surfing`. It modifies the `calculate_cost` method to add an extra charge for surfing and provides a custom description.

- **AdventureTrip (Child Class):** Inherits from `VacationPackage` and introduces the attribute `difficulty_level`. If the difficulty is set to 'hard', the total cost is doubled.

- **LuxuryCruise (Child Class):** Inherits from `VacationPackage` with the extra attribute `has_private_suite`. The cost increases by 50% if the suite is included.

## Methods

### `calculate_cost()`
This method is implemented differently in each subclass to account for the unique cost calculation rules for each vacation type:

- **BeachResort:** Adds a fixed charge for surfing.
- **AdventureTrip:** Doubles the cost for difficult trips.
- **LuxuryCruise:** Adds a 50% premium for private suites.

### `describe_package()`
This method returns a description of the vacation package, customized for each subclass. It includes details about the destination, duration, and specific features (e.g., surfing or private suite).


### Defensive Programming
Throughout our implementation we use defensive programming to ensure the correct function of all out classes and functions. For instance in the `VacationPackage_new` function we assert that the destination argument passed into the function is a string. This makes our code easier to debug and less prone to errors.

## Example Usage

You can create instances of the vacation types using the `make` function, and invoke methods to calculate costs or describe the package.

```python
beach_resort = make(BeachResort, "Maldives", 100, 7, True)
print(call(beach_resort, 'calculate_cost'))  # Outputs the total cost of the Beach Resort package
print(call(beach_resort, 'describe_package'))  # Outputs the description of the Beach Resort package

adventure_trip = make(AdventureTrip, "Macchu Picchu", 150, 4, "easy")
print(call(adventure_trip, 'calculate_cost'))  # Outputs the total cost of the Adventure Trip package
print(call(adventure_trip, 'describe_package'))  # Outputs the description of the Adventure Trip package

luxury_cruise = make(LuxuryCruise, "Mediterranean", 100, 14, False)
print(call(luxury_cruise, 'calculate_cost'))  # Outputs the total cost of the Luxury Cruise package
print(call(luxury_cruise, 'describe_package'))  # Outputs the description of the Luxury Cruise package
```

## Conclusion

This part of the vacation booking system successfully makew the system flexible and allows for the addition of new vacation types and customization of methods as needed, without changing the code structure.

## Part 2 Documentation

### `booked_vacations` List for Tracking Objects

A global list `booked_vacations` is used to store the vacation packages that are instantiated during the program execution. This list allows us to keep track of all the created vacation objects and is useful when interacting with global variables from different scripts. The `add_to_booked_vacations` function reads through the global scope and adds any vacation package dictionaries (with a key named `destination`) to the `booked_vacations` list.

### `find_booked_vacations` helper function for  calculate_total_cost and extract_total_vacation_summary functions

The find booked vacations function is used as a helper function to find instantiated vacations. It accepts an optional `search_term` argument which allows for the specification of the output vacation type. The function will return any instantiated vacations whose names contain the `search_term`. If no `search_term` is specified all instantiated vacations will be returned. We made the decision to separate the booked_vacations list from the find_booked_vacations function to make the list part of the global scope instead of the local scope.

### `calculate_total_cost` function

The `calculate_total_cost` first retrieves all relevant instantiated vacation objects using the `find_booked_vacations` function. Then it iterates through the booked vacation objects and uses the `call` function and `calculate_cost()` method to retrieve the cost of each. Finally it sums all the costs and returns the total cost. 

### `extract_total_vacation_summary` function

The `extract_total_vacation_summary` first retrieves all relevant instantiated vacation objects using the `find_booked_vacations` function. Then it iterates through the booked vacation objects and uses the `call` function and `describe_package()` method to retrieve the summary of each. Finally it concatenates all the descriptions together and returns the resulting string.

## Example Usage

You can create instances of the vacation types using the `make` function, and invoke methods to calculate costs or describe the package.

```python
# All Instantiated Vacations
VacationBookingSummary1 = make(VacationBookingSummary)
print(call(VacationBookingSummary1, 'extract_total_vacation_summary', VacationBookingSummary1["search_term"]))

# All Vacations, search_term = 'adventure'
current_search_term = 'adventure'
VacationBookingSummary2 = make(VacationBookingSummary, current_search_term)
print("The total cost is:", call(VacationBookingSummary2, 'calculate_total_cost', VacationBookingSummary2["search_term"]))
```

### Parts 1 & 2 sample outputs
Each time the vacation_booking.py is ran on its own it also executes a series of print statements which output some sample calculations and descriptions. This code is there to prove that our code is running correclty, and all the features are implemented without errors.

## Part 3 Documentation

## Tests
`test_vacation_booking.py` contains unit tests targeting the main functionalities of the Vacation Types classes as well as integration tests targeting the Vacation Booking Summary class.

For the sake of consistency and ease of testing, all mock vacations are set to have

- `destination` = Tenerife
- `cost_per_day` = 100
- `duration_in_days` = 5

as defined in `setUp()`.

### Vacation Type Tests

#### Beach Resort Tests

- **test_calculate_cost_beachResort...() :** These tests calculate the cost of a Beach Resort vacation with or without `surfing_included` as an additional service.

- **test_describe_beachResort...() :** These tests check the correctness of the description for a Beach Resort vacation booked either with or without `surfing_included`.

#### Adventure Trip Tests

- **test_calculate_cost_adventureTrip...() :** These tests calculate the cost of an Adventure Trip with `difficulty_level` being either 'easy' or 'hard'.

- **test_describe_adventureTrip...() :** These tests check the correctness of the description for an Adventure Trip with `difficulty_level` being either 'easy' or 'hard'.

#### Luxury Cruise Tests

- **test_calculate_cost_luxuryCruise...() :** These tests calculate the cost of a Luxury Cruise vacation with or without `has_private_suite` included.

- **test_describe_luxuryCruise...() :** These tests check the correctness of the description for a Luxury Cruise vacation with or without `has_private_suite` included.


### Vacation Booking Summary Tests

- **test_calculate_total_cost_all_vacations() :** This test calculates the total cost of all vacations booked in the Vacation Booking System.

- **test_calculate_total_cost_beachResort_vacations() :** This test calculates the total cost of all Beach Resort vacations booked in the Vacation Booking System.

- **test_extract_total_vacation_summary_beachResort_vacations() :** This test checks the correctness of descriptions for all Beach Resort vacations booked either with or without `surfing_included` in the Vacation Booking System.

## Running Tests

### Batch Run Tests
All tests can be run in one batch by running the `run_tests()` method in `test_vacation_booking.py`.

### Run Individual or A Combination of Tests
Alternatively, an individual or a combination of tests can also be run from the Terminal using the command

```terminal
python test_vacation_booking.py --select <keyword>
```

which runs all tests whose method contains the provided `<keyword>`.

For example, in order to run all the 6 possible Beach Resort related tests, we can use the command

```terminal
python test_vacation_booking.py --select resort
```

### Summary Output From Running Tests
For each test ran under `test_vacation_booking.py`, the
- test name
- runtime in seconds
- test result

gets printed in the Terminal as in the below example:

```terminal
--- test_calculate_cost_adventureTrip_easy: 0.0 seconds, pass ---
--- test_calculate_cost_adventureTrip_hard: 0.0 seconds, pass ---

 Summary:
- Pass: 2 tests
- Fail: 0 tests
- Error: 0 tests
```

`Pass` indicates a successful test, `Fail` indicates the failure of a synthetically valid test, and `Error` refers to a test which could not be executed to to some code Exception.