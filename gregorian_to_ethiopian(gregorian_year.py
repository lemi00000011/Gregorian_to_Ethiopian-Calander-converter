def gregorian_to_ethiopian(gregorian_year, gregorian_month, gregorian_day):
    # Gregorian to Ethiopian calendar conversion
    # Ethiopian calendar has 13 months in a leap year and 12 months otherwise
    # The start of the Ethiopian year is on September 11 or 12 (depending on leap year)

    # Gregorian calendar constants
    gregorian_start_year = 1900  # Gregorian calendar starts from year 1900

    # Ethiopian calendar constants
    ethiopian_start_year = 1900  # Ethiopian calendar equivalent to Gregorian year 1900
    ethiopian_start_day = 11  # Ethiopian calendar starts from September 11 or 12
    ethiopian_months_normal = [
        "Meskerem", "Tikemet", "Hidar", "Tahsas", "Tir", "Yekatit",
        "Megabit", "Miazia", "Genbot", "Sene", "Hamle", "Nehase", "Pagumē"
    ]
    ethiopian_months_leap = [
        "Meskerem", "Tikemet", "Hidar", "Tahsas", "Tir", "Yekatit",
        "Megabit", "Miazia", "Genbot", "Sene", "Hamle", "Nehase", "Pagumē"
    ]

    # Calculate the day difference from the start of the Gregorian calendar
    gregorian_days = 0
    for year in range(gregorian_start_year, gregorian_year):
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            gregorian_days += 366  # Leap year
        else:
            gregorian_days += 365  # Non-leap year

    # Add days for the current year
    leap_year = (gregorian_year % 4 == 0 and gregorian_year % 100 != 0) or (gregorian_year % 400 == 0)
    days_in_month = [31, 29 if leap_year else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for month in range(1, gregorian_month):
        gregorian_days += days_in_month[month - 1]

    # Add remaining days in the current month
    gregorian_days += gregorian_day - 1

    # Calculate the Ethiopian year, month, and day from the total days count
    ethiopian_days = gregorian_days + ethiopian_start_day - 1
    ethiopian_year = ethiopian_start_year + ethiopian_days // 365
    ethiopian_day_of_year = ethiopian_days % 365

    # Determine if the Ethiopian year is a leap year
    ethiopian_leap = (ethiopian_year - 1) % 4 == 3

    # Determine the Ethiopian month and day
    if ethiopian_leap:
        ethiopian_months = ethiopian_months_leap
    else:
        ethiopian_months = ethiopian_months_normal

    ethiopian_month = 1
    while ethiopian_day_of_year >= days_in_month[ethiopian_month - 1]:
        ethiopian_day_of_year -= days_in_month[ethiopian_month - 1]
        ethiopian_month += 1

    ethiopian_day = ethiopian_day_of_year + 1

    return ethiopian_year, ethiopian_months[ethiopian_month - 1], ethiopian_day

# Example usage:
gregorian_year = 2024
gregorian_month = 6
gregorian_day = 16
ethiopian_year, ethiopian_month, ethiopian_day = gregorian_to_ethiopian(gregorian_year, gregorian_month, gregorian_day)
print(f"Gregorian date: {gregorian_day}/{gregorian_month}/{gregorian_year}")
print(f"Ethiopian date: {ethiopian_day} {ethiopian_month} {ethiopian_year} (in Amharic)")
