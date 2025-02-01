
from datetime import datetime, timedelta


def convert_date(year, day_of_year):
    """
    Converts a year and day of the year to an ISO 8601 formatted date.

    :param year: The year (e.g., 2020).
    :param day_of_year: The day of the year (1-365 or 1-366 for leap years).
    :return: ISO 8601 formatted date string (e.g., "2020-01-01T00:00:00").
    """
    try:
        # Create the first day of the given year
        first_day = datetime(year, 1, 1)

        # Add the offset of days to the first day of the year
        target_date = first_day + timedelta(days=day_of_year - 1)

        # Return the date in ISO 8601 format
        return target_date.isoformat()
    except Exception as e:
        return f"Error: {e}"
