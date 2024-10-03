import logging
from datetime import datetime
from typing import Any

logging.basicConfig(
    filename="../logs/services.log",
    filemode="a",
    format="%(asctime)s: %(name)s: %(levelname)s: %(message)s",
    level=logging.INFO,
    encoding="utf-8",
    force=True,
)

logger = logging.getLogger(__name__)


def investment_bank(month: str, transactions: list[dict[str, Any]], limit: int = 50) -> float:
    """The function of receiving income through investment_bank."""

    logger.info(f"Запуск функции {investment_bank.__name__}.")
    target_date_obj = datetime.strptime(month, "%Y-%m")
    savings = 0.00
    try:
        for transaction in transactions:
            date_str = datetime.strptime(transaction["Дата операции"], "%d.%m.%Y %H:%M:%S").strftime("%Y-%m-%d")
            date_obj = datetime.strptime(date_str, "%Y-%m-%d")
            if target_date_obj.year == date_obj.year and target_date_obj.month == date_obj.month:
                round_up = limit - transaction["Сумма операции"] % limit
                savings += round_up
        logger.info(f"Успешное завершение работы функции {investment_bank.__name__}.")
        return round(savings, 2)
    except Exception as e:
        logger.error(f"Завершение функции {investment_bank.__name__} с ошибкой {e}.")
        return round(savings, 2)
