from datetime import datetime, timedelta


def calculate_review_dates(start_date):
    """
    Calculate spaced repetition review dates based on an initial study date.

    Args:
        start_date (datetime): The date of the first study session.

    Returns:
        list[int]: A list of four spaced repetition review dates (day numbers only). Each subsequent review is spaced at double
        the interval of the previous one, considering month-end wrap-around.

    Example:
        >>> calculate_review_dates(datetime(1))
        [2, 4, 8, 16]

        >>> calculate_review_dates(datetime(31))  # Start date is the last day of a month
        [1, 3, 7, 15]

        >>> calculate_review_dates(datetime(28))  # Start date in February of a non-leap year
        [1, 3, 7, 15]

        >>> calculate_review_dates(datetime(30))  # Start date near the year-end
        [31, 2, 6, 14]
    """
    review_dates = []
    days_to_next_review = 1  # Days to the next review start at 1

    for _ in range(4):
        next_review_date = start_date + timedelta(
            days=days_to_next_review
        )  # Adjust review interval
        review_dates.append(next_review_date.day)
        days_to_next_review *= 2  # Double the interval for the next review

    return review_dates
