def calculate_review_days(start_day):
    """
    Calculate spaced repetition review days based on an initial study day.

    Args:
        start_day (int): The day of the initial study session (1-31).

    Returns:
        list[int]: A list of four spaced repetition review days. Each subsequent review is spaced at double
        the interval of the previous one, ignoring month and year changes.

    Examples:
        >>> calculate_review_days(1)
        [2, 4, 8, 16]

        >>> calculate_review_days(15)
        [16, 18, 22, 30]

        >>> calculate_review_days(30)
        [31, 2, 6, 14]

        >>> calculate_review_days(31)
        [1, 3, 7, 15]
    """
    review_days = []  # Initialize an empty list to store review days
    days_to_next_review = 1  # Start with 1 day to the first review

    for _ in range(4):  # Loop to calculate four review days
        # Calculate the next review day, wrapping around a 31-day cycle
        next_review_day = (start_day + days_to_next_review - 1) % 31 + 1
        review_days.append(next_review_day)  # Add the calculated day to the list
        days_to_next_review *= 2  # Double the interval for the next review

    return review_days  # Return the list of review days
