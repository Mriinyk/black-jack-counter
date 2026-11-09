"""Тест точки входу головного файлу."""
from app import main


def test_main_is_callable():
    assert callable(main.main)