from LunarLander import burn_fuel, change_velocity, change_altitude
"""test with pytest"""

# input (lines 51-56) commented out to test
def test_burn_normal():
    assert burn_fuel(0, 100) == 0
    assert burn_fuel(70, 100) == 70


def test_burn_neg():
    assert burn_fuel(100, -100) == 0
    assert burn_fuel(100, -10) == 0


def test_burn_to_and_over_limit():
    assert burn_fuel(100, 101) == 100
    assert burn_fuel(100, 200) == 100


def test_changev_norm():
    assert change_velocity(0.0, 0.15, 10) == 0.1
    assert change_velocity(4.3, 0.15, 30) == 1.4


def test_changev_to_neg():
    assert change_velocity(0.0, 0.15, 100) == -13.4
    assert change_velocity(5.0, 0.15, 200) == -23.4


def test_change_alt():
    assert change_altitude(100, 100) == 0
    assert change_altitude(100, 1000) == 900
    assert change_altitude(100, 200) == 100