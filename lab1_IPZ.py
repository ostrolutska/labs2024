# Функція для розрахунку чисел Фібоначчі
def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_value = fib_sequence[i - 1] + fib_sequence[i - 2]
        fib_sequence.append(next_value)
    return fib_sequence

# Користувач вводить кількість чисел для розрахунку
n = int(input("Введіть кількість чисел Фібоначчі для виведення: "))
fib_sequence = fibonacci(n)

# Виводимо результат
print(f"Перші {n} чисел Фібоначчі: {fib_sequence}")
