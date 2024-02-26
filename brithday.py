def days_since_birthday(birthday_date):
    # Extract the birth year from the date string
    birth_year = int(birthday_date.split('-')[-1])
    current_year = 2024  # Consider the current year to be 2024

    num_whole_years = current_year - birth_year - 1

    # Initialize the total days counter
    total_days = 0

    # Calculate the number of days in each of the whole years since the birth year
    for year in range(birth_year + 1, current_year):
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            # Leap year has 366 days
            total_days += 366
        else:
            # Non-leap year has 365 days
            total_days += 365

    return total_days
