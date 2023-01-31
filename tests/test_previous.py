import pytest
from fiscal_calendar_helper.helper import Fiscal_Helper
fiscal = Fiscal_Helper()

def test_previous_week_valid():
    assert fiscal.previous('2023_01') == '2022_52'

def test_previous_date_valid():
    assert fiscal.previous('2023_01_01') == '2022_12_31'

def test_previous_invalid():
    with pytest.raises(ValueError):
        fiscal.previous('invalid')
