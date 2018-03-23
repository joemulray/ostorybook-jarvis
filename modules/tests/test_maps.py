import modules


def test_maps():
    assert ('maps' == modules.process_query('Open maps')[0])
    assert ('maps' == modules.process_query('Directions to <Location>')[0])
    assert ('maps' == modules.process_query('Can you get me directions to <Location>?')[0])
    assert ('maps' != modules.process_query('Take me home')[0])
