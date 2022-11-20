digits = ["12", "145", "  45", "12.4", "45,14", "15 645"]


def process(i):
    i = i.strip()
    i = i.replace(",", ".")
    i = i.replace(" ", "")
    i = float(i)
    return i


right_digits = map(process, digits)

print(list(right_digits))