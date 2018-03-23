import modules


def test_rideservices():
    assert ('rideservices' == modules.process_query('I need a ride')[0])
    assert ('rideservices' == modules.process_query('Call me an <Uber/Lyft>')[0])
    assert ('rideservices' == modules.process_query('Can you drive me home?')[0])
    assert ('rideservices' != modules.process_query('Can you order me an <Uber/Lyft>')[0])
