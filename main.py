
def task_1():
    n = int(input("Введите количество городов -> "))
    prices = list(map(int, input("Введите цены через пробел -> ").split()))
    
    for i in range(n):
        found = -1
        for j in range(i + 1, n):
            if prices[j] < prices[i]:
                found = j
                break
        print(found)

while True:
    n = input()
    
    print(
        (
            "0 - Выход\n"
            "1 - Задача 1"
        )
    )
    if n == "0":
        break
    elif n == "1":
        task_1()
    else:
        print("Нет такой задачи")