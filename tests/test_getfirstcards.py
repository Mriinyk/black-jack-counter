"""Тести для GetFirstCards."""
from app.logic.getfirstcards import GetFirstCards


def test_blackjack():
    assert GetFirstCards(["A", "K"]).calculate_sum() == 21


def test_ten_and_ace():
    assert GetFirstCards(["10", "A"]).calculate_sum() == 21


def test_two_number_cards():
    assert GetFirstCards(["2", "3"]).calculate_sum() == 5


def test_face_card_value():
    assert GetFirstCards(["Q", "7"]).calculate_sum() == 17


def test_multiple_aces_over_21():
    # 11 + 11 -> 12, потім + 10 -> 22 (туз уже не зменшує суму)
    assert GetFirstCards(["A", "A", "K"]).calculate_sum() == 22


def test_three_aces():
    assert GetFirstCards(["A", "A", "A"]).calculate_sum() == 13