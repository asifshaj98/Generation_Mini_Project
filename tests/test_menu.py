from unittest.mock import patch, MagicMock, Mock
from unittest import mock
from src.functions import Menu

def test_main_menu_inputs():
    mock_args = ["1"]
    with mock.patch("builtins.input") as mock_input:
        mock_input.side_effect = mock_args
        result = Menu().main_menu()
    assert result == "1"

def test_products_menu_inputs():
    mock_args = ["1"]
    with mock.patch("builtins.input") as mock_input:
        mock_input.side_effect = mock_args
        result = Menu().products_menu()
    assert result == "1"

def test_order_menu_inputs():
    mock_args = ["1"]
    with mock.patch("builtins.input") as mock_input:
        mock_input.side_effect = mock_args
        result = Menu().order_menu()
    assert result == "1"

def test_courier_menu_input():
    mock_args = ["1"]
    with mock.patch("builtins.input") as mock_input:
        mock_input.side_effect = mock_args
        result = Menu().courier_menu()
    assert result == "1"