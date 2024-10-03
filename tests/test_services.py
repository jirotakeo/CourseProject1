from src.services import investment_bank


def test_investment_bank(operation_list):
    assert investment_bank("2018-02", operation_list, 50) == 88.0
    assert investment_bank("2019-01", operation_list, 50) == 45.0
    assert investment_bank("2019-03", operation_list, 50) == 9.0
