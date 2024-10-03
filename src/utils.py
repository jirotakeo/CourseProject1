import logging
import os
from collections import Counter
from datetime import datetime

import pandas as pd
import requests
from dotenv import load_dotenv

load_dotenv()
api_key1 = os.getenv("API_KEY")
api_key2 = os.getenv("API_KEY2")

headers1 = {"apikey": api_key1}
headers2 = {"apikey": api_key2}


logging.basicConfig(
    filename="../logs/utils.log",
    filemode="w",
    format="%(asctime)s: %(name)s: %(levelname)s: %(message)s",
    level=logging.INFO,
    encoding="utf-8",
)

logger = logging.getLogger(__name__)


def get_greeting(date_str: str) -> str:
    """Function get greeting by time."""
    logger.info(f"Запуск функции {get_greeting.__name__}.")
    try:
        time_obj = datetime.strptime(date_str, "%d.%m.%Y %H:%M:%S")
        if 5 <= time_obj.hour < 12:
            greeting = "Доброе утро"
        elif 12 <= time_obj.hour < 17:
            greeting = "Добрый день"
        elif 17 <= time_obj.hour < 23:
            greeting = "Добрый вечер"
        else:
            greeting = "Доброй ночи"
        logger.info(f"Успешное завершение работы функции {get_greeting.__name__}.")
        return greeting
    except Exception as e:
        logger.error(f"Завершение работы функции {get_greeting.__name__} с ошибкой {e}.")


def get_data_from_xlsx(filename: str) -> pd.DataFrame:
    """The function gets data from a xlsx file and returns a dataframe"""
    logger.info(f"Запуск функции {get_data_from_xlsx.__name__}.")
    try:
        result = pd.read_excel(filename).fillna(0)
        logger.info(f"Успешное завершение работы функции {get_data_from_xlsx.__name__}.")
        return result
    except Exception as e:
        logger.error(f"Завершение работы функции {get_data_from_xlsx.__name__} с ошибкой {e}.")


def filtered_by_date(current_date: str, df: pd.DataFrame) -> pd.DataFrame:
    """Function filter operations since beginning of month till current date."""
    logger.info(f"Запуск функции {filtered_by_date.__name__}.")
    try:
        end_date = datetime.strptime(current_date, "%d.%m.%Y %H:%M:%S")
        start_date = datetime.strptime(f"01.{end_date.month}.{end_date.year} 00:00:00", "%d.%m.%Y %H:%M:%S")
        df["Дата"] = df["Дата операции"].map(lambda x: datetime.strptime(str(x), "%d.%m.%Y %H:%M:%S"))
        filtered_df = df[(df["Дата"] >= start_date) & (df["Дата"] <= end_date)]
        logger.info(f"Успешное завершение работы функции {filtered_by_date.__name__}.")
        return filtered_df.iloc[:, :-1]
    except Exception as e:
        logger.error(f"Завершение работы функции {filtered_by_date.__name__} с ошибкой {e}.")


def get_data_about_cards(df_data: pd.DataFrame) -> list[dict]:
    """Function get data about user cards from DataFrame."""
    logger.info(f"Запуск функции {get_data_about_cards.__name__}.")
    try:
        cards_list = list(Counter(df_data.loc[:, "Номер карты"]))
        cards_data = []
        for card in cards_list:
            j_df_data = df_data.loc[df_data.loc[:, "Номер карты"] == card]
            total_spent = abs(sum(j for j in j_df_data.loc[:, "Сумма операции"] if j < 0))
            cashback = round(total_spent / 100, 2)
            cards_data.append({"last_digits": card, "total_spent": total_spent, "cashback": cashback})
        logger.info(f"Успешное завершение работы функции {get_data_about_cards.__name__}.")
        return cards_data
    except Exception as e:
        logger.error(f"Завершение работы функции {get_data_about_cards.__name__} с ошибкой {e}.")


def get_top_transactions(df_data: pd.DataFrame, top_number=5) -> list[dict]:
    """Function get top-5 transactions from DataFrame."""
    logger.info(f"Запуск функции {get_top_transactions.__name__}.")
    try:
        top_transactions_list = []
        df = df_data.loc[::]
        df["amount"] = df.loc[:, "Сумма платежа"].map(float).map(abs)
        sorted_df_data = df.sort_values(by="amount", ascending=False, ignore_index=True)
        for i in range(top_number):
            date = sorted_df_data.loc[i, "Дата платежа"]
            amount = float(sorted_df_data.loc[i, "amount"])
            category = sorted_df_data.loc[i, "Категория"]
            description = sorted_df_data.loc[i, "Описание"]
            top_transactions_list.append(
                {"date": date, "amount": amount, "category": category, "description": description}
            )
        logger.info(f"Успешное завершение работы функции {get_top_transactions.__name__}.")
        return top_transactions_list
    except Exception as e:
        logger.error(f"Завершение работы функции {get_top_transactions.__name__} с ошибкой {e}.")


def get_currency_rates(currencies_list: list[str]):
    """Function get currency rates."""
    result = {}
    logger.info(f"Запуск функции {get_currency_rates.__name__}.")
    try:
        url = "https://api.apilayer.com/exchangerates_data/latest"
        for i in currencies_list:
            payload = {"symbols": "RUB", "base": f"{i}"}
            response = requests.get(url, headers=headers1, params=payload)
            courses = response.json()
            result[i] = courses["rates"]["RUB"]
        logger.info(f"Успешное завершение работы функции {get_currency_rates.__name__}.")
        return result
    except Exception as e:
        logger.error(f"Завершение работы функции {get_currency_rates.__name__} с ошибкой {e.__repr__()}.")


def get_stock_rates(stock_list: list[str]):
    """Function get stock rates."""
    result = []
    logger.info(f"Запуск функции {get_stock_rates.__name__}.")
    try:
        url = f"https://financialmodelingprep.com/api/v3/stock/list?apikey={api_key2}"
        response = requests.get(url, headers=headers2)
        stocks = response.json()
        print(stocks)
        df = pd.DataFrame(stocks).loc[:"symbol"]
        for i in stock_list:
            ldf = df.loc[df.symbol == i]
            result.append({"stock": i, "price": round(float(ldf.price.iloc[0]), 2)})
        logger.info(f"Успешное завершение работы функции {get_stock_rates.__name__}.")
        return result
    except Exception as e:
        logger.error(f"Завершение работы функции {get_stock_rates.__name__} с ошибкой {e}.")
