from fiscal_calendar_helper.helper import Fiscal_Helper
fiscal = Fiscal_Helper()

def test_next_week():
    assert fiscal.next('2022_52') == '2023_01'
