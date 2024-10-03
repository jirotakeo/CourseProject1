import json
import logging
from datetime import datetime

from src.utils import (filtered_by_date, get_currency_rates, get_data_about_cards, get_data_from_xlsx, get_greeting,
                       get_stock_rates, get_top_transactions)

user_settings_path = "../user_settings.json"

logging.basicConfig(
    filename="../logs/utils.log",
    filemode="w",
    format="%(asctime)s: %(name)s: %(levelname)s: %(message)s",
    level=logging.INFO,
    encoding="utf-8",
)

logger = logging.getLogger(__name__)


def main_page(date: str) -> str:
    """Function get info for main page."""
    logger.info(f"Запуск функции {main_page.__name__}.")
    try:
        data_xlsx = get_data_from_xlsx("../data/operations.xlsx")
        date_format = datetime.strptime(date, "%Y-%m-%d %H:%M:%S").strftime("%d.%m.%Y %H:%M:%S")
        with open(user_settings_path) as f:
            user_settings = json.load(f)
        currency_list = user_settings["user_currencies"]
        stock_list = user_settings["user_stocks"]
        filtered_df = filtered_by_date(date_format, data_xlsx)
        greeting = get_greeting(date_format)
        cards_info = get_data_about_cards(filtered_df)
        top_transactions = get_top_transactions(filtered_df)
        currency_rates = get_currency_rates(currency_list)
        stock_rates = get_stock_rates(stock_list)
        main_page_info = json.dumps(
            {
                "greeting": greeting,
                "cards": cards_info,
                "top_transactions": top_transactions,
                "currency_rates": currency_rates,
                "stock_prices": stock_rates,
            },
            ensure_ascii=False,
        )
        logger.info(f"Успешное завершение работы функции {main_page.__name__}.")
        return main_page_info
    except Exception as e:
        logger.error(f"Завершение работы функции {main_page.__name__} с ошибкой {e}.")
