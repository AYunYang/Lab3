import price_info

def test_total_cost_of_shopping():

    total_cost = price_info.total_cost_shopping()
    assert(total_cost == 46.75)



def test_apple_cost_of_fruits():

    result = price_info.cost_of_fruits('apple',10)
    assert(result == 12)