# Atharv Kolhar
# Python Bytes


"""
Flight Itinerary:
Given an unordered list of flights taken by someone,
each represented as (origin, destination) pairs,
and a starting airport, compute the person's itinerary.
If no such itinerary exists, return null.
If there are multiple possible itineraries, return the lexicographically smallest one.
All flights must be used in the itinerary.

For example, given the list of flights
[('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')]
and starting airport 'YUL', you should return the list ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'].

Given the list of flights [('SFO', 'COM'), ('COM', 'YYZ')] and starting airport 'COM',
you should return null.

Given the list of flights [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')] and
starting airport 'A', you should return the list ['A', 'B', 'C', 'A', 'C']
even though ['A', 'C', 'A', 'B', 'C'] is also a valid itinerary.
However, the first one is lexicographically smaller.
"""


def flight_order(flight_list, origin, flight_route=None):

    if flight_route is None:
        flight_route = []

    possible_flight = []

    for flight in flight_list:
        if origin == flight[0]:
            possible_flight.append(flight)

    if not possible_flight:
        return 'Null'

    possible_flight.sort()

    flight_taken = possible_flight[0]

    if not flight_route:
        flight_route = [origin]

    flight_route.append(flight_taken[1])
    flight_list.remove(flight_taken)

    if flight_list:
        res = flight_order(flight_list, flight_taken[1], flight_route)
        if res == 'Null':
            return 'Null'

    return flight_route


if __name__ == '__main__':
    print(flight_order([('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')], 'YUL'))

    print(flight_order([('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')], 'A'))

    print(flight_order([('SFO', 'COM'), ('COM', 'YYZ')], 'COM'))
