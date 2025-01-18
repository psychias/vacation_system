from vacation_booking import *
from typing import List
import time
import sys


def setUp():
    """
    Instantiates mock vacations and booking summaries to be used for unit and integration tests.
    
    Parameters:
        None.
    
    Returns:
        None.
    """
    global beach_resort_no_surfing
    global beach_resort_with_surfing
    global adventure_trip_easy
    global adventure_trip_hard
    global luxury_cruise_no_private_suite
    global luxury_cruise_has_private_suite
    global vacation_booking_summary
    global beach_resort_booking_summary
    
    beach_resort_no_surfing = make(BeachResort, 'Tenerife', 100, 5, False)
    beach_resort_with_surfing = make(BeachResort, 'Tenerife', 100, 5, True)
    adventure_trip_easy = make(AdventureTrip, 'Tenerife', 100, 5, 'easy')
    adventure_trip_hard = make(AdventureTrip, 'Tenerife', 100, 5, 'hard')
    luxury_cruise_no_private_suite = make(LuxuryCruise, 'Tenerife', 100, 5, False)
    luxury_cruise_has_private_suite = make(LuxuryCruise, 'Tenerife', 100, 5, True)
    vacation_booking_summary = make(VacationBookingSummary)
    beach_resort_booking_summary = make(VacationBookingSummary, "beach")

    add_to_booked_vacations()


def tearDown():
    """
    Deletes all instantiated mock vacations and booking summaries.
    
    Parameters:
        None.
    
    Returns:
        None.
    """
    global beach_resort_no_surfing
    global beach_resort_with_surfing
    global adventure_trip_easy
    global adventure_trip_hard
    global luxury_cruise_no_private_suite
    global luxury_cruise_has_private_suite
    global vacation_booking_summary
    global beach_resort_booking_summary
    
    del beach_resort_no_surfing
    del beach_resort_with_surfing
    del adventure_trip_easy
    del adventure_trip_hard
    del luxury_cruise_no_private_suite
    del luxury_cruise_has_private_suite
    del vacation_booking_summary
    del beach_resort_booking_summary


def add_to_booked_vacations():
    """
    Appends instantiated mock vacation classes to be stored in booked_vacations list from vacation_booking.py.
    
    Parameters:
        None.
    
    Returns:
        None.
    """
    for (name, _dict) in globals().items():
        if isinstance(_dict, dict):
            if "destination" in _dict.keys(): 
                booked_vacations.append(_dict)
    return 

# Beach Resort Tests
def test_calculate_cost_beachResort_without_surfing():
    """
    Tests the cost calculation of a Beach Resort vacation without surfing_included.
    
    Parameters:
        None.
    
    Returns:
        True if the assertion is correct.

    Raises:
        AssertionError of the assertion is not correct.
    """
    assert calculate_cost_beachResort(beach_resort_no_surfing) == 500

def test_calculate_cost_beachResort_with_surfing():
    """
    Tests the cost calculation of a Beach Resort vacation with surfing_included.
    
    Parameters:
        None.
    
    Returns:
        True if the assertion is correct.

    Raises:
        AssertionError of the assertion is not correct.
    """
    assert calculate_cost_beachResort(beach_resort_with_surfing) == 600

def test_describe_beachResort_without_surfing():
    """
    Tests the description of a Beach Resort vacation without surfing_included.
    
    Parameters:
        None.
    
    Returns:
        True if the assertion is correct.

    Raises:
        AssertionError of the assertion is not correct.
    """
    assert describe_beachResort(beach_resort_no_surfing) == "The 5 day long BeachResort vacation in Tenerife does not include surfing."

def test_describe_beachResort_with_surfing():
    """
    Tests the description of a Beach Resort vacation with surfing_included.
    
    Parameters:
        None.
    
    Returns:
        True if the assertion is correct.

    Raises:
        AssertionError of the assertion is not correct.
    """
    assert describe_beachResort(beach_resort_with_surfing) == "The 5 day long BeachResort vacation in Tenerife includes surfing."

# Adventure Trip Tests
def test_calculate_cost_adventureTrip_easy():
    """
    Tests the cost calculation of an Adventure Trip with easy difficulty_level.
    
    Parameters:
        None.
    
    Returns:
        True if the assertion is correct.

    Raises:
        AssertionError of the assertion is not correct.
    """
    assert calculate_cost_adventureTrip(adventure_trip_easy) == 500

def test_calculate_cost_adventureTrip_hard():
    """
    Tests the cost calculation of an Adventure Trip with hard difficulty_level.
    
    Parameters:
        None.
    
    Returns:
        True if the assertion is correct.

    Raises:
        AssertionError of the assertion is not correct.
    """
    assert calculate_cost_adventureTrip(adventure_trip_hard) == 1000

def test_describe_adventureTrip_easy():
    """
    Tests the description of an Adventure Trip with easy difficulty_level.
    
    Parameters:
        None.
    
    Returns:
        True if the assertion is correct.

    Raises:
        AssertionError of the assertion is not correct.
    """
    assert describe_adventureTrip(adventure_trip_easy) == "The 5 day long AdventureTrip in Tenerife is considered easy."

def test_describe_adventureTrip_hard():
    """
    Tests the description of an Adventure Trip with hard difficulty_level.
    
    Parameters:
        None.
    
    Returns:
        True if the assertion is correct.

    Raises:
        AssertionError of the assertion is not correct.
    """
    assert describe_adventureTrip(adventure_trip_hard) == "The 5 day long AdventureTrip in Tenerife is considered hard."

# Luxury Cruise Tests
def test_calculate_cost_luxuryCruise_no_private_suite():
    """
    Tests the cost calculation of a Luxury Cruise vacation with no private suite.
    
    Parameters:
        None.
    
    Returns:
        True if the assertion is correct.

    Raises:
        AssertionError of the assertion is not correct.
    """
    assert calculate_cost_luxuryCruise(luxury_cruise_no_private_suite) == 500

def test_calculate_cost_luxuryCruise_has_private_suite():
    """
    Tests the cost calculation of a Luxury Cruise vacation no private suite.
    
    Parameters:
        None.
    
    Returns:
        True if the assertion is correct.

    Raises:
        AssertionError of the assertion is not correct.
    """
    assert calculate_cost_luxuryCruise(luxury_cruise_has_private_suite) == 750

def test_describe_luxuryCruise_no_private_suite():
    """
    Tests the description of a Luxury Cruise vacation with no private suite.
    
    Parameters:
        None.
    
    Returns:
        True if the assertion is correct.

    Raises:
        AssertionError of the assertion is not correct.
    """
    assert describe_luxuryCruise(luxury_cruise_no_private_suite) == "The 5 day long LuxuryCruise in Tenerife does not include a private suite."

def test_describe_luxuryCruise_has_private_suite():
    """
    Tests the description of a Luxury Cruise vacation with private suite.
    
    Parameters:
        None.
    
    Returns:
        True if the assertion is correct.

    Raises:
        AssertionError of the assertion is not correct.
    """
    assert describe_luxuryCruise(luxury_cruise_has_private_suite) == "The 5 day long LuxuryCruise in Tenerife includes a private suite."

# Vacation Booking Summary Tests
def test_calculate_total_cost_all_vacations():
    """
    Tests if the total cost of all vacations booked in the Vacation Booking System is correct.
    
    Parameters:
        None.
    
    Returns:
        True if the assertion is correct.

    Raises:
        AssertionError of the assertion is not correct.
    """
    assert call(vacation_booking_summary, 'calculate_total_cost', vacation_booking_summary["search_term"]) == 3850

def test_calculate_total_cost_beachResort_vacations():
    """
    Tests if the total cost of all Beach Resort vacations booked in the Vacation Booking System is correct.
    
    Parameters:
        None.
    
    Returns:
        True if the assertion is correct.

    Raises:
        AssertionError of the assertion is not correct.
    """
    assert call(beach_resort_booking_summary, 'calculate_total_cost', beach_resort_booking_summary["search_term"]) == 1100

def test_extract_total_vacation_summary_beachResort_vacations():
    """
    Tests if the descriptions of all Beach Resort vacations booked in the Vacation Booking System is correct.
    
    Parameters:
        None.
    
    Returns:
        True if the assertion is correct.

    Raises:
        AssertionError of the assertion is not correct.
    """
    msg = "The 5 day long BeachResort vacation in Tenerife does not include surfing." + '\n' + "The 5 day long BeachResort vacation in Tenerife includes surfing." + '\n'
    assert call(beach_resort_booking_summary, 'extract_total_vacation_summary', beach_resort_booking_summary["search_term"]) == msg


def run_tests() -> None:
    """
    Batch runs all tests under test_vacation_booking.py.
    
    Parameters:
        None.
    
    Returns:
        None
    """
    setUp()
    
    pattern = None
    if "--select" in sys.argv:
        assert len(sys.argv) == 3, "Incorrect number of system arguments"
        pattern = sys.argv[2].lower()
    else:
        assert len(sys.argv) < 2, "Unrecognized system argument"
    
    state = {"pass": 0, "fail": 0, "error": 0}
    
    for (name, test) in globals().items():
        if not name.startswith("test_"):
            continue
        if pattern and (pattern not in name.lower()):
            continue
        try:
            start_time = time.time()
            test()
            execution_time = round((time.time() - start_time), 4)
            current_state = "pass"
            state[current_state] += 1

        except AssertionError:
            execution_time = round((time.time() - start_time), 4)
            current_state = "fail"
            state[current_state] += 1

        except Exception as ex:
            execution_time = round((time.time() - start_time), 4)
            current_state = "error"
            state[current_state] += 1
            print(f'this is the error -> {ex}')

        print(f"--- {test.__name__}: {execution_time} seconds, {current_state} ---")

    print("\n Summary:")
    print(f"- Pass: {state['pass']} tests")
    print(f"- Fail: {state['fail']} tests")
    print(f"- Error: {state['error']} tests")

    tearDown()

if __name__ == '__main__':
    run_tests()
