import pytest

from tesla import Tesla

def test_color_check():
    # CHECK IF TESLA HAS RIGHT COLOR
    new_car = Tesla("3", "red")
    assert new_car.color == "red"
def test_seats_change():
    # TRIES TO UNLOCK TESLA
    new_car = Tesla("3", "red")
    new_car.seats_count = 6
    assert new_car.seats_count == 6
