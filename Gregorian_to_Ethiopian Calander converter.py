import ethiopian_date

def convert_to_ethiopian(year, month, day):
  """Converts a Gregorian date to Ethiopian date and returns it in Amharic format.

  Args:
      year: Gregorian year (int).
      month: Gregorian month (int).
      day: Gregorian day (int).20

  Returns:
      A string representing the Ethiopian date in Amharic format.
  """

  # Convert Gregorian date to Ethiopian date
  ethiopian_date = EthiopianDate.from_gregorian(year, month, day)

  # Extract components
  ethiopian_year = ethiopian_date.year
  ethiopian_month = ethiopian_date.month_name  # Amharic month name
  ethiopian_day = ethiopian_date.day

  # Print the date in Amharic format
  return f"{ethiopian_day} ቀን፣ {ethiopian_month} ወር፣ {ethiopian_year} ዓመተ ምህረት"

# Get user input for Gregorian date
while True:
  try:
    gregorian_year = int(input("Enter Gregorian year (YYYY): "))
    gregorian_month = int(input("Enter Gregorian month (MM): "))
    gregorian_day = int(input("Enter Gregorian day (DD): "))
    break
  except ValueError:
    print("Invalid input. Please enter numbers only.")

# Convert and display Ethiopian date
ethiopian_date_str = convert_to_ethiopian(gregorian_year, gregorian_month, gregorian_day)
print(f"\nYour entered Gregorian date corresponds to:\n{ethiopian_date_str}")
