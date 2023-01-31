import pytest
from fiscal_calendar_helper.helper import Fiscal_Helper
fiscal = Fiscal_Helper()

def test_next_week_valid():
    assert fiscal.next('2022_52') == '2023_01'

def test_next_date_valid():
    assert fiscal.next('2022_12_31') == '2023_01_01'

def test_next_invalid():
    with pytest.raises(ValueError):
        fiscal.next('invalid')
