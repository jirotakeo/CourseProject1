import os
from unittest.mock import patch

import pytest
from pandas import DataFrame

from src.utils import (filtered_by_date, get_currency_rates, get_data_about_cards, get_data_from_xlsx, get_greeting,
                       get_stock_rates, get_top_transactions)


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("01.01.2023 07:30:20", "Доброе утро"),
        ("01.01.2023 13:00:00", "Добрый день"),
        ("01.01.2023 20:15:04", "Добрый вечер"),
        ("01.01.2023 00:00:00", "Доброй ночи"),
    ],
)
def test_get_greeting(input_data, expected):
    assert get_greeting(input_data) == expected


@patch("src.utils.pd.read_excel")
def test_get_data_from_excel(mock_read_excel, empty_df):
    mock_read_excel.return_value = empty_df
    assert get_data_from_xlsx("test.xlsx").equals(empty_df)
    mock_read_excel.assert_called_once_with("test.xlsx")


def test_get_data_about_cards(test_operations):
    assert get_data_about_cards(test_operations) == [{"last_digits": "*7197", "total_spent": 224.89, "cashback": 2.25}]


def test_filter_by_date(transactions_df_test_1):
    df = DataFrame(
        {
            "Дата операции": ["01.08.2024 18:00:00"],
            "Сумма операции": ["-160.89"],
            "Категория": ["Супермаркеты"],
        }
    )
    assert filtered_by_date("07.08.2024 18:00:05", transactions_df_test_1).equals(df)


def test_get_top_transactions(top_5):
    assert get_top_transactions(top_5, 2) == [
        {"date": "31.12.2019", "amount": 17000, "category": "Услуги банка", "description": "Колхоз"},
        {"date": "31.12.2020", "amount": 4575.45, "category": "Фастфуд", "description": "Колхоз"},
    ]


url = "https://api.apilayer.com/exchangerates_data/latest"
apikey = os.getenv("API_KEY")
payload = {"symbols": "RUB", "base": "EUR"}


@patch("requests.get")
def test_get_currency_rates(mock_get):
    mock_get.return_value.json.return_value = {"rates": {"RUB": 104.460878}}
    assert get_currency_rates(["EUR"]) == {"EUR": 104.460878}
    mock_get.assert_called_once_with(url, headers={"apikey": apikey}, params=payload)


apikey2 = os.getenv("API_KEY2")
url2 = os.getenv("test_url")


@patch("requests.get")
def test_get_stock_rates(mock_get):
    mock_get.return_value.json.return_value = [{"symbol": "HALO.NE", "price": 0.02}]
    assert get_stock_rates(["HALO.NE"]) == [{"stock": "HALO.NE", "price": 0.02}]
    mock_get.assert_called_once_with(url2, headers={"apikey": apikey2})
