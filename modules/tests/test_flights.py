import modules


def test_flights():
    assert ('flights' == modules.process_query('Find me cheap flights')[0])
    assert ('flights' == modules.process_query('Find me a flight home')[0])
    assert ('flights' == modules.process_query('Can you find me a flight from <Location> to <Location>')[0])
    assert ('flights' != modules.process_query('Flights to <Location> from <Location>')[0])
