import math 

# list to save the instances of the vocation objects instances 
booked_vacations = []

def make(cls, *args):
    """
    Creates an instance of a given class by calling its '_new' method with the provided arguments.
    
    Parameters:
        cls (dict): The class dictionary containing methods and attributes.
        *args: Arguments passed to the class constructor.
    
    Returns:
        dict: An instance of the class with the initialized attributes.
    """
    instance = cls["_new"](*args)
    return instance

def call(thing, key_name, *args):
    """
    Calls a method of a class instance based on the method name.
    
    Parameters:
        thing (dict): The class instance (object).
        key_name (str): The method name to be called.
        *args: Arguments passed to the method.
    
    Returns:
        The result of the method call.
    """
    method = find(thing["_class"], key_name)
    return method(thing, *args)

def find(cls, key_name):
    """
    Searches for a method in a class and its parent classes.
    
    Parameters:
        cls (dict): The class dictionary where the method is searched for.
        key_name (str): The name of the method to find.
    
    Returns:
        function: The found method function.
    
    Raises:
        NotImplementedError: If the method is not found in the class or its parents.
    """
    if key_name in cls:
        return cls[key_name]
    if cls["_parent"]:
        return find(cls["_parent"], key_name)
    raise NotImplementedError("Missing method " + key_name)

def calculate_cost():
    """
    Placeholder function for calculating vacation cost.
    
    Raises:
        NotImplementedError: Since the function is not implemented yet.
    """
    raise NotImplementedError('this function is not implemented')

def describe_package():
    """
    Placeholder function for describing a vacation package.
    
    Raises:
        NotImplementedError: Since the function is not implemented yet.
    """
    raise NotImplementedError('this function is not implemented')

def VacationPackage_new(destination, cost_per_day, duration_in_days):
    """
    Constructor for a generic vacation package.
    
    Parameters:
        destination (str): The destination of the vacation.
        cost_per_day (int): The daily cost of the vacation.
        duration_in_days (int): The duration of the vacation in days.
    
    Returns:
        dict: The newly created vacation package instance.
    """
    assert isinstance(destination, str), f'the var destination must be type str'
    assert isinstance(cost_per_day, int), f'the var cost_per_day must be type int'
    assert isinstance(duration_in_days, int), f'the var duration_in_days must be type int'

    return {
        'destination': destination,
        'cost_per_day': cost_per_day,
        'duration_in_days': duration_in_days,
        '_class': VacationPackage
    }

VacationPackage = {
    'calculate_cost': calculate_cost,
    'describe_package': describe_package,
    '_classname': 'VacationPackage',
    '_parent': None,
    '_new': VacationPackage_new
}

# Beach Resort

def beachResort_new(destination, cost_per_day, duration_in_days, includes_surfing):
    """
    Constructor for a Beach Resort vacation package.

    Parameters:
        destination (str): The destination of the beach resort.
        cost_per_day (int): The daily cost of the vacation.
        duration_in_days (int): The duration of the vacation in days.
        includes_surfing (bool): Whether the package includes surfing.
    
    Returns:
        dict: The newly created beach resort instance.
    """
    assert isinstance(includes_surfing, bool), f"The var includes_surfing should be type boolean"
    return make(VacationPackage, destination, cost_per_day, duration_in_days) | {
        "includes_surfing": includes_surfing,
        "_class": BeachResort
    }

def calculate_cost_beachResort(thing):
    """
    Calculates the total cost of the beach resort vacation, with an additional cost if surfing is included.
    
    Parameters:
        thing (dict): The beach resort instance.
    
    Returns:
        int: The total cost of the vacation.
    """
    cost = thing['cost_per_day'] * thing['duration_in_days']
    if thing['includes_surfing']: cost += 100
    return cost

def describe_beachResort(thing):
    """
    Provides a description of the beach resort vacation.
    
    Parameters:
        thing (dict): The beach resort instance.
    
    Returns:
        str: A description of the vacation.
    """
    base = f"The {thing['duration_in_days']} day long {thing['_class']['_classname']} vacation in {thing['destination']} "
    if thing['includes_surfing']:
        return base + "includes surfing."
    return base + "does not include surfing."

BeachResort = {
    'calculate_cost': calculate_cost_beachResort,
    'describe_package': describe_beachResort,
    '_parent': VacationPackage,
    '_classname': 'BeachResort',
    '_new': beachResort_new
}

# Adventure Trip

def adventureTrip_new(destination, cost_per_day, duration_in_days, difficulty_level):
    """
    Constructor for an Adventure Trip vacation package.
    
    Parameters:
        destination (str): The destination of the adventure trip.
        cost_per_day (int): The daily cost of the vacation.
        duration_in_days (int): The duration of the vacation in days.
        difficulty_level (str): The difficulty level of the trip.
    
    Returns:
        dict: The newly created adventure trip instance.
    """
    assert isinstance(difficulty_level, str), f"The var difficulty_level should be type string"
    return make(VacationPackage, destination, cost_per_day, duration_in_days) | {
        "difficulty_level": difficulty_level,
        "_class": AdventureTrip
    }

def calculate_cost_adventureTrip(thing):
    """
    Calculates the total cost of the adventure trip vacation, doubling the cost if the difficulty level is 'hard'.
    
    Parameters:
        thing (dict): The adventure trip instance.
    
    Returns:
        int: The total cost of the vacation.
    """
    cost = thing['cost_per_day'] * thing['duration_in_days']
    if thing['difficulty_level'] == 'hard': cost *= 2
    return cost

def describe_adventureTrip(thing):
    """
    Provides a description of the adventure trip vacation.
    
    Parameters:
        thing (dict): The adventure trip instance.
    
    Returns:
        str: A description of the vacation.
    """
    return f"The {thing['duration_in_days']} day long {thing['_class']['_classname']} in {thing['destination']} is considered {thing['difficulty_level']}."

AdventureTrip = {
    'calculate_cost': calculate_cost_adventureTrip,
    'describe_package': describe_adventureTrip,
    '_parent': VacationPackage,
    '_classname': 'AdventureTrip',
    '_new': adventureTrip_new
}

# Luxury Cruise

def luxuryCruise_new(destination, cost_per_day, duration_in_days, has_private_suite):
    """
    Constructor for a Luxury Cruise vacation package.
    
    Parameters:
        destination (str): The destination of the luxury cruise.
        cost_per_day (int): The daily cost of the vacation.
        duration_in_days (int): The duration of the vacation in days.
        has_private_suite (bool): Whether the cruise includes a private suite.
    
    Returns:
        dict: The newly created luxury cruise instance.
    """
    assert isinstance(has_private_suite, bool), f"The var has_private_suite should be type boolean"
    return make(VacationPackage, destination, cost_per_day, duration_in_days) | {
        "has_private_suite": has_private_suite,
        "_class": LuxuryCruise
    }

def calculate_cost_luxuryCruise(thing):
    """
    Calculates the total cost of the luxury cruise vacation, increasing the cost by 50% if a private suite is included.
    
    Parameters:
        thing (dict): The luxury cruise instance.
    
    Returns:
        int: The total cost of the vacation.
    """
    cost = thing['cost_per_day'] * thing['duration_in_days']
    if thing['has_private_suite']: cost *= 1.5
    return cost

def describe_luxuryCruise(thing):
    """
    Provides a description of the luxury cruise vacation.
    
    Parameters:
        thing (dict): The luxury cruise instance.
    
    Returns:
        str: A description of the vacation.
    """
    base = f"The {thing['duration_in_days']} day long {thing['_class']['_classname']} in {thing['destination']} "
    if thing['has_private_suite']:
        return base + "includes a private suite."
    return base + "does not include a private suite."

LuxuryCruise = {
    'calculate_cost':calculate_cost_luxuryCruise,
    'describe_package':describe_luxuryCruise,
    '_parent':VacationPackage,
    '_classname': 'LuxuryCruise',
    '_new':luxuryCruise_new
}

# VacationBookingSummary

def add_to_booked_vacations():
    """
    Adds all globally defined vacation instances (dictionaries) that have a 'destination' key to the booked_vacations list.
    
    Returns:
        None
    """
    for (name, _dict) in globals().items():
        if isinstance(_dict, dict):
            if "destination" in _dict.keys(): 
                booked_vacations.append(_dict)
    return

def find_booked_vacations(search_term):
    """
    Finds vacations from the booked_vacations list based on a search term.
    
    Parameters:
        search_term (str): A search term to filter vacations by type.
    
    Returns:
        list: A list of vacation instances that match the search term.
    """
    results = []
    for vacation in globals().get("booked_vacations", []):
        vacation_type = vacation["_class"]["_classname"].lower()
        if search_term is None or search_term in vacation_type:
            results.append(vacation)
    return results

def calculate_total_cost(thing, search_term):
    """
    Calculates the total cost of all booked vacations that match the search term.
    
    Parameters:
        thing (dict): The vacation booking summary instance.
        search_term (str): A search term to filter vacations by type.
    
    Returns:
        int: The total cost of all matching vacations.
    """
    result = find_booked_vacations(search_term)
    total_cost = 0
    for vacation in result:
        vacation_cost = call(vacation, "calculate_cost")
        total_cost += vacation_cost
    return total_cost

def extract_total_vacation_summary(thing, search_term):
    """
    Extracts a detailed description of all booked vacations that match the search term.
    
    Parameters:
        thing (dict): The vacation booking summary instance.
        search_term (str): A search term to filter vacations by type.
    
    Returns:
        str: A concatenated description of all matching vacations.
    """
    booked_vacations = find_booked_vacations(search_term)
    total_description = ""
    for vacation in booked_vacations:
        vacation_description = call(vacation, "describe_package")
        total_description += vacation_description + "\n"
    return total_description

def VacationBookingSummary_new(search_term=None):
    """
    Constructor for a vacation booking summary.
    
    Parameters:
        search_term (str): A search term to filter vacations by type (optional).
    
    Returns:
        dict: A new vacation booking summary instance.
    """
    return {
        'search_term': search_term,
        '_class': VacationBookingSummary
    }

VacationBookingSummary = {
    'calculate_total_cost': calculate_total_cost,
    'extract_total_vacation_summary': extract_total_vacation_summary,
    '_classname': "VacationBookingSummary",
    '_parent': None,
    '_new': VacationBookingSummary_new
}


if __name__ == '__main__':
    
    # Part 1 Outputs
    beach_resort = make(BeachResort, 'Maldives', 100, 7, False)
    adventure_trip = make(AdventureTrip, "Macchu Picchu", 150, 4, "easy")
    adventure_trip2 = make(AdventureTrip, "Macchu Picchu", 150, 4, "hard")
    luxury_cruise = make(LuxuryCruise, "Mediterranean", 100, 14, False)
    add_to_booked_vacations()


    print("\n","Part 1 Outputs:","\n")

    print(calculate_cost_beachResort(beach_resort))
    print(describe_beachResort(beach_resort))
    print(describe_adventureTrip(adventure_trip))
    print(describe_luxuryCruise(luxury_cruise))

    # Part 2 Outputs
    current_search_term = 'adventure'
    VacationBookingSummary1 = make(VacationBookingSummary)
    VacationBookingSummary2 = make(VacationBookingSummary, current_search_term)

    print("\n","Part 2 Outputs:","\n")

    # Summary of all Instantiated Vacations
    print("Summary of all Instantiated Vacations")
    print("The total cost is:", call(VacationBookingSummary1, 'calculate_total_cost', VacationBookingSummary1["search_term"]))
    print(call(VacationBookingSummary1, 'extract_total_vacation_summary', VacationBookingSummary1["search_term"]))

    # Summary of all current_search_term Vacations
    print(f"Summary of all {current_search_term} Vacations")
    print("The total cost is:", call(VacationBookingSummary2, 'calculate_total_cost', VacationBookingSummary2["search_term"]))
    print(call(VacationBookingSummary2, 'extract_total_vacation_summary', VacationBookingSummary2["search_term"]))
