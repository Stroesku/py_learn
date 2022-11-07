"""
     не самый оптимальный вариант потому что чем больше будет срок, тем больше вычислений будет произведено
     при расчете полугодового вклада будет 5 итераций а для пятилетней - 60
"""

def compound(amount, year_percent, months):
    month_percent = year_percent / 12
    for i in range(months):
        inc = amount / 100 * month_percent
        amount += inc
    return amount

# более оптимальный вариант
def capitalization(sum, percent, months):
    k = (1 + percent / 100 / 12)
    result = sum * k ** months
    return result.__round__()


print(capitalization(10000, 10, 12))
