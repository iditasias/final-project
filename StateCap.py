import pytest
from termcolor import colored

STATES_CAPITALS = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock',
    'California': 'Sacramento',
    'Colorado': 'Denver',
    'Connecticut': 'Hartford',
    'Delaware': 'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
    'Hawaii': 'Honolulu',
    'Idaho': 'Boise',
    'Illinois': 'Springfield',
    'Indiana': 'Indianapolis',
    'Iowa': 'Des Moines',
    'Kansas': 'Topeka',
    'Kentucky': 'Frankfort',
    'Louisiana': 'Baton Rouge',
    'Maine': 'Augusta',
    'Maryland': 'Annapolis',
    'Massachusetts': 'Boston',
    'Michigan': 'Lansing',
    'Minnesota': 'Saint Paul',
    'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City',
    'Montana': 'Helena',
    'Nebraska': 'Lincoln',
    'Nevada': 'Carson City',
    'New Hampshire': 'Concord',
    'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe',
    'New York': 'Albany',
    'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck',
    'Ohio': 'Columbus',
    'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem',
    'Pennsylvania': 'Harrisburg',
    'Rhode Island': 'Providence',
    'South Carolina': 'Columbia',
    'South Dakota': 'Pierre',
    'Tennessee': 'Nashville',
    'Texas': 'Austin',
    'Utah': 'Salt Lake City',
    'Vermont': 'Montpelier',
    'Virginia': 'Richmond',
    'Washington': 'Olympia',
    'West Virginia': 'Charleston',
    'Wisconsin': 'Madison',
    'Wyoming': 'Cheyenne',
}


def capital_of_state(state):
    print('Capital of ' + colored(state, 'red') + ' is ' + colored((STATES_CAPITALS[state]), 'green'))


def get_state(capital):
    for key, value in STATES_CAPITALS.items():
        if capital == value:
            return key


def state_of_capital(capital):
    print('State of ' + colored(capital, 'red') + ' is ' + colored(get_state(capital), 'green'))


def all_states():
    print('All States:')
    for key in STATES_CAPITALS.keys():
        print(key)


def all_capitals():
    print('All Capitals:')
    for value in STATES_CAPITALS.values():
        print(value)


def states_capitals_string():
    print('States and Capitals in a string:')
    string = ''
    for key, value in STATES_CAPITALS.items():
        string += (key + ' -> ' + value + ' , ')
    print(string[:len(string)])


user_input = str("")

while user_input != "9":
    user_input = input("""Select option:
        1. What's the name of the capital of states in US?
        2. What's the name of the states in US when the capital is?
        3. Print all states.
        4. Print all capitals.
        5. Create a single string 'Alabama -> Montgomery, Alaska -> Juneau, ...'
        9. Exit\n """)

    if user_input == "1":  # capital of states
        state = input("Enter the state to find the capitol: ")
        capital_of_state(state)
        wait = input("Press Enter to continue.")

    if user_input == "2":  # state of capital
        capital = input("Enter the capital to find the state: ")
        state_of_capital(capital)
        wait = input("Press Enter to continue.")

    if user_input == "3":  # all states
        all_states()

    if user_input == "4":  # all capitals
        all_capitals()

    if user_input == "5":  # string of states and capitols
        states_capitals_string()

print('The state of Madison Capital city = ' + get_state('Madison'))


def test_state_to_capital():
    assert 'Cheyenne' == STATES_CAPITALS['Wyoming']


def test_state_to_capital_unknown():
    with pytest.raises(KeyError):
        STATES_CAPITALS['']


def test_capital_to_state():
    assert 'Wyoming' == get_state('Cheyenne')


def test_capital_to_state_unknown():
    with pytest.raises(KeyError):
        raise KeyError
