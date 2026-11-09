"""Тести для CountSystem."""
from app.logic.countsystem import CountSystem


def test_count_current_score():
    score = CountSystem()
    assert score.count_current_score("5") == 1.5
    assert score.count_current_score("K") == 0.5
    assert score.count_current_score("8") == 0.5
    assert score.count_current_score("A") == -0.5


def test_count_unknown_card_ignored():
    score = CountSystem()
    assert score.count_current_score("X") == 0.0


def test_true_score_normal():
    score = CountSystem()
    score.count_current_score("5", "5")  # 3.0
    assert score.true_score(52) == 3.0


def test_true_score_zero_cards():
    score = CountSystem()
    assert score.true_score(0) == "Карти закінчилися"