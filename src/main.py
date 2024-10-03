import datetime

from src.views import main_page


def main():
    """Main function."""

    date_obj = datetime.datetime.now() - datetime.timedelta(days=365 * 3)
    today = date_obj.strftime("%Y-%m-%d %H:%M:%S")
    main_page(today)


if __name__ == "__main__":
    main()
