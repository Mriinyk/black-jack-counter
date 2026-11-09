"""Тести для ux_settings.uxsettings."""
from app.ux_settings.uxsettings import ColorForInfo
from colorama import Fore


def test_color_for_true_count_red():
    result = ColorForInfo().color_for_true_count(0.5)
    assert result.startswith(Fore.RED)


def test_color_for_true_count_white():
    result = ColorForInfo().color_for_true_count(1.0)
    assert result.startswith(Fore.WHITE)


def test_color_for_true_count_yellow():
    result = ColorForInfo().color_for_true_count(3.0)
    assert result.startswith(Fore.YELLOW)


def test_color_for_true_count_cyan():
    result = ColorForInfo().color_for_true_count(7.0)
    assert result.startswith(Fore.CYAN)


def test_color_for_true_count_magenta():
    result = ColorForInfo().color_for_true_count(12.0)
    assert result.startswith(Fore.MAGENTA)