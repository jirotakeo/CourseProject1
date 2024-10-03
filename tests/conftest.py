import json

import pytest
from pandas import DataFrame


@pytest.fixture()
def transactions_df_test_1():
    df = DataFrame(
        {
            "Дата операции": [
                "01.08.2024 18:00:00",
                "19.07.2024 05:00:00",
                "20.06.2024 16:00:00",
                "31.12.2019 07:00:00",
                "31.12.2018 08:00:00",
            ],
            "Сумма операции": ["-160.89", "-64.0", "-4575.45", "-17000.0", "-5.05"],
            "Категория": ["Супермаркеты", "Супермаркеты", "Фастфуд", "Ж/Д билеты", "Переводы"],
        }
    )
    return df


@pytest.fixture()
def empty_df():
    em_df = DataFrame(
        {
            "Дата операции": [],
            "Дата платежа": [],
            "Номер карты": [],
            "Статус": [],
            "Сумма операции": [],
            "Валюта операции": [],
            "Сумма платежа": [],
            "Валюта платежа": [],
            "Кэшбэк": [],
            "Категория": [],
            "МСС": [],
            "Описание": [],
            "Бонусы (включая кэшбэк)": [],
            "Округление на инвесткопилку": [],
            "Сумма операции с округлением": [],
        }
    )
    return em_df


@pytest.fixture()
def test_operations():
    df = DataFrame(
        {
            "Дата операции": ["31.12.2021  16:44:00", "31.12.2021  16:42:04"],
            "Дата платежа": ["31.12.2021", "31.12.2021"],
            "Номер карты": ["*7197", "*7197"],
            "Статус": ["OK", "OK"],
            "Сумма операции": [-160.89, -64],
            "Валюта операции": ["RUB", "RUB"],
            "Сумма платежа": [-160.89, -64],
            "Валюта платежа": ["RUB", "RUB"],
            "Кэшбэк": ["", ""],
            "Категория": ["Супермаркеты", "Супермаркеты"],
            "МСС": ["5411", "5411"],
            "Описание": ["Колхоз", "Колхоз"],
            "Бонусы (включая кэшбэк)": ["3", "1"],
            "Округление на инвесткопилку": ["0", "0"],
            "Сумма операции с округлением": ["160,89", "64"],
        }
    )
    return df


@pytest.fixture()
def top_5():
    df = DataFrame(
        {
            "Дата операции": [
                "31.12.2021  16:44:00",
                "31.12.2021  16:42:04",
                "31.12.2020  16:42:04",
                "31.12.2019  16:42:04",
                "31.12.2018  16:42:04",
            ],
            "Дата платежа": ["31.12.2021", "31.12.2021", "31.12.2020", "31.12.2019", "31.12.2018"],
            "Номер карты": ["*7197", "*7197", "*7851", "*7851", "*4521"],
            "Статус": ["OK", "OK", "OK", "OK", "OK"],
            "Сумма операции": ["-160.89", "-64", "-4575.45", "-17000", "-5.05"],
            "Валюта операции": ["RUB", "RUB", "RUB", "RUB", "RUB"],
            "Сумма платежа": ["-160.89", "-64", "-4575.45", "-17000", "-5.05"],
            "Валюта платежа": ["RUB", "RUB", "RUB", "RUB", "RUB"],
            "Кэшбэк": ["", "", "", "", ""],
            "Категория": ["Супермаркеты", "Супермаркеты", "Фастфуд", "Услуги банка", "Переводы"],
            "МСС": ["5411", "5411", "5411", "5411", "5411"],
            "Описание": ["Колхоз", "Колхоз", "Колхоз", "Колхоз", "Колхоз"],
            "Бонусы (включая кэшбэк)": ["3", "1", "", "", ""],
            "Округление на инвесткопилку": ["0", "0", "0", "0", "0"],
            "Сумма операции с округлением": ["160,89", "64", "4575.75", "17000", "5.05"],
        }
    )
    return df


@pytest.fixture()
def operation_list():
    op_list = [
        {"Дата операции": "01.02.2018 00:00:00", "Сумма операции": 1712},
        {"Дата операции": "01.01.2019 00:00:00", "Сумма операции": 55},
        {"Дата операции": "12.02.2018 00:00:00", "Сумма операции": 50},
        {"Дата операции": "12.03.2019 00:00:00", "Сумма операции": 41},
    ]
    return op_list


@pytest.fixture()
def transactions_df_test():
    df = DataFrame(
        {
            "Дата операции": [
                "01.08.2024 00:00:00",
                "19.07.2024 00:00:00",
                "20.06.2024 00:00:00",
                "31.12.2019 00:00:00",
                "31.12.2018 00:00:00",
            ],
            "Сумма операции": [-160.89, -64.0, -4575.45, -17000.0, -5.05],
            "Категория": ["Супермаркеты", "Супермаркеты", "Фастфуд", "Ж/Д билеты", "Переводы"],
            "Статус": ["OK", "OK", "OK", "OK", "OK"],
        }
    )
    return df


@pytest.fixture()
def json_response():
    response = json.dumps(
        {
            "greeting": "Доброй ночи",
            "cards": [{"last digits": "*7777", "total_spent": 88888.01, "cashback": 88.88}],
            "top_transactions": [
                {
                    "date": "2024.05.02 05:02:00",
                    "amount": 17000,
                    "category": "Супермаркеты",
                    "description": "Выброшенные на ветер деньги",
                }
            ],
            "currency_rates": [{"currency": "USD", "price": 22}],
            "stock_prices": [{"stock": "AAPL", "price": 111.11}],
        },
        ensure_ascii=False,
    )
    return response
