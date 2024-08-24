# The python program that calculate pay rate
# Author: Kayla Ahreum Kim
# Date Created: 20/9/2021

try:
    # Define variables
    workHour = 0.0
    payRate = 0.0

    # User input variables
    workHour = float(input('Enter the number of hours worked: '))
    payRate = float(input('Enter the hourly pay rate: '))
    print('\u001b[0m', end = '')

    # Analyze variables
    if (workHour < 0) or (payRate <= 0):
        print('You have entered wrong number.')
        quit()

    # Calculate gross payment
    if workHour > 40:
        grossPay = workHour * (payRate * 1.5)
    else:
        grossPay = workHour * payRate

    # Print result
    print(f'The gross pay is ${grossPay:.2f}')

except ValueError as valueE:
    print(valueE)

except Exception as e:
    print(e)