import modules


def test_shopping():
    assert ('shopping' == modules.process_query('Can you order me a smart bulb')[0])
    assert ('shopping' == modules.process_query('Show me smartbulbs')[0])
    assert ('shopping' == modules.process_query('Can you show me smartbulbs?')[0])
    assert ('shopping' != modules.process_query('Show me stuff thats on sale')[0])
