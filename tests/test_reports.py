from pandas import DataFrame

from src.reports import spending_by_category


def test_spending_by_category(transactions_df_test):
    df = DataFrame(
        {
            "Дата операции": ["01.08.2024 00:00:00", "19.07.2024 00:00:00"],
            "Сумма операции": [-160.89, -64.0],
            "Категория": ["Супермаркеты", "Супермаркеты"],
            "Статус": ["OK", "OK"],
        }
    )
    assert spending_by_category(transactions_df_test, "Супермаркеты").equals(df)
