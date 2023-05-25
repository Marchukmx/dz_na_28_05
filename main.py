#2

def average_closure():
    total = 0
    count = 0

    def add_number(number):
        nonlocal total, count
        total += number
        count += 1

    def get_average():
        if count == 0:
            return 0
        return total / count

    return add_number, get_average

add, average = average_closure()
add(100)
add(21)
add(124314)
print(average())
