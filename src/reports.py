import logging
from datetime import datetime, timedelta
from typing import Optional

import pandas as pd

logging.basicConfig(
    filename="../logs/reports.log",
    filemode="w",
    format="%(asctime)s: %(name)s: %(levelname)s: %(message)s",
    level=logging.INFO,
    encoding="utf-8",
)

logger = logging.getLogger(__name__)


def report(filename):
    """Decorator create report file."""

    def my_decorator(func):

        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(filename, "w", encoding="utf-8") as file:
                result.to_json(file, orient="records", force_ascii=False)
            return result

        return wrapper

    return my_decorator


def spending_by_category(transactions: pd.DataFrame, category: str, date: Optional[str] = None) -> pd.DataFrame:
    """The function returns expenses for a given category"""

    logger.info(f"Запуск функции {spending_by_category.__name__}")
    if date:
        date_obj = datetime.strptime(date, "%d.%m.%Y")
    else:
        date_obj = datetime.now().date()
    end_date = date_obj.strftime("%Y.%m.%d")

    transactions["Дата"] = transactions["Дата операции"].map(lambda x: datetime.strptime(str(x), "%d.%m.%Y %H:%M:%S"))
    begin_date = (date_obj - timedelta(days=90)).strftime("%Y.%m.%d")
    tr_by_cat = transactions.loc[transactions.loc[:, "Категория"] == category]
    tr_by_cat_period = tr_by_cat[(tr_by_cat["Дата"] >= begin_date) & (tr_by_cat["Дата"] <= end_date)]
    tr_by_cat_status = tr_by_cat_period.loc[transactions.loc[:, "Статус"] == "OK"].iloc[:, :-1]
    res = tr_by_cat_status.loc[transactions.loc[:, "Сумма операции"] <= 0]
    logger.info(f"Успешное завершение работы функции {spending_by_category.__name__}")
    return res
