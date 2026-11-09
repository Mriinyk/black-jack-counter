"""Тести для GetExtraCard."""
from app.logic.getextracard import GetExtraCard


def test_extra_ace_when_safe():
    assert GetExtraCard(["A"], 10).calculate_new_sum() == 21


def test_extra_ace_converts_to_one():
    assert GetExtraCard(["A"], 11).calculate_new_sum() == 12


def test_extra_number_card():
    assert GetExtraCard(["5"], 15).calculate_new_sum() == 20


def test_extra_multiple_cards():
    assert GetExtraCard(["2", "3"], 10).calculate_new_sum() == 15


def test_extra_ace_over_21():
    # 10 + 11 = 21, потім + 11 = 32 > 21 → один туз перелічується як 1: 22
    assert GetExtraCard(["A", "A"], 10).calculate_new_sum() == 22