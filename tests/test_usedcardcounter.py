"""Тести для UsedTracker."""
from app.logic.usedcardcounter import UsedTracker


def test_initial_remaining_cards():
    tracker = UsedTracker(1)
    assert tracker.remaining_cards == 52


def test_remaining_cards_multiple_decks():
    tracker = UsedTracker(2)
    assert tracker.remaining_cards == 104


def test_update_marks_cards():
    tracker = UsedTracker(1)
    tracker.update("2", "2", "K")
    assert tracker.used_cards["2"] == 2
    assert tracker.used_cards["K"] == 1
    assert tracker.remaining_cards == 49


def test_percentage_contains_percent_sign():
    tracker = UsedTracker(1)
    tracker.update("A")
    result = tracker.percentage_of_cards
    assert "%" in result
    assert "A" in result


def test_percentage_when_no_cards_left():
    tracker = UsedTracker(1)
    all_cards = []
    for rank in ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]:
        all_cards.extend([rank] * 4)
    tracker.update(*all_cards)
    assert tracker.remaining_cards == 0
    assert tracker.percentage_of_cards == "Карти закінчилися"