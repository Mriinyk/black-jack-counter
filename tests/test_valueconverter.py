"""Тести для value_converter."""
from app.logic.valueconverter import value_converter


def test_convert_face_cards():
    assert value_converter(["K", "Q", "J", "A"]) == [10, 10, 10, 11]


def test_convert_number_cards():
    assert value_converter(["2", "7", "10"]) == [2, 7, 10]


def test_convert_lowercase():
    assert value_converter(["k", "q", "a"]) == [10, 10, 11]


def test_convert_mixed():
    assert value_converter(["A", "2", "K"]) == [11, 2, 10]


def test_unknown_cards_are_skipped():
    assert value_converter(["A", "X", "2", "?"]) == [11, 2]


def test_empty_list():
    assert value_converter([]) == []