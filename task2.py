import re
from typing import Callable

def generator_numbers(text: str) -> list:
    pattern = '([0-9]+(?:\\.[0-9]+)?)(?:\\s)'
    list = re.findall(pattern, text)
    return list

def sum_profit(text: str, func: Callable):
    incomes = func(text)
    sum = 0

    for income in incomes:
        sum = sum + float(income)

    return sum

text = 'Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів.'
total_income = sum_profit(text, generator_numbers)
print(f'Загальний дохід: {total_income}')