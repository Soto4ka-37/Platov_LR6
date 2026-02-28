# ЗАДАЧА 1
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

# ЗАДАЧА 2
def task_2():
    queue = []
    while True:
        command = input().split()
        
        if command[0] == 'push':
            if len(command) < 2:
                print('error')
                continue
            queue.append(int(command[1]))
            print('ok')
        
        elif command[0] == 'pop':
            if len(queue) == 0:
                print('error')
            else:
                print(queue.pop(0))
        
        elif command[0] == 'front':
            if len(queue) == 0:
                print('error')
            else:
                print(queue[0])
        
        elif command[0] == 'size':
            print(len(queue))
        
        elif command[0] == 'clear':
            queue.clear()
            print('ok')
        
        elif command[0] == 'exit':
            print('bye')
            break

# ЗАДАЧА 3
def task_3():
    parts = input("Введите коэффициенты -> ").split()
    coefficients = list(map(float, parts))
    roots = []
    
    if len(coefficients) == 1:
        c = coefficients[0]
        if c == 0:
            roots = []
    
    elif len(coefficients) == 2:
        b, c = coefficients
        if b != 0:
            roots = [-c / b]
    
    elif len(coefficients) == 3:
        a, b, c = coefficients
        if a == 0:
            if b != 0:
                roots = [-c / b]
        else:
            D = b * b - 4 * a * c
            if D == 0:
                roots = [-b / (2 * a)]
            elif D > 0:
                x1 = (-b - D ** 0.5) / (2 * a)
                x2 = (-b + D ** 0.5) / (2 * a)
                roots = [x1, x2]
    
    roots.sort()
    print(*roots)

# ЗАДАЧА 4
def task_4():
    first = list(map(int, input("Введите карты первого игрока -> ").split()))
    second = list(map(int, input("Введите карты второго игрока -> ").split()))
    
    moves = 0
    
    while len(first) > 0 and len(second) > 0:
        moves += 1
        
        card1 = first.pop(0)
        card2 = second.pop(0)
        
        if card1 > card2:
            first.append(card1)
            first.append(card2)
        else:
            second.append(card2)
            second.append(card1)
    
    if len(first) > 0:
        print("first")
    else:
        print("second")
    
    print(moves)

# ЗАДАЧА 5
class Rectangle:
    def __init__(self, width, height):
        self.Width = width
        self.Height = height
    
    def GetArea(self):
        return self.Width * self.Height
    
    def GetPerimeter(self):
        return 2 * (self.Width + self.Height)
    
    def ToString(self):
        return f"Rectangle {self.Width}x{self.Height}"
    
def task_5():
    width, height = map(int, input("Введите ширину и высоту -> ").split())
    rect = Rectangle(width, height)
    print(rect.GetArea())
    print(rect.GetPerimeter())
    print(rect.ToString())
    
# ОСНОВНАЯ ПРОГРАММА
while True:
    print(
        (
            "0 - Выход\n"
            "1 - Задача 1\n"
            "2 - Задача 2\n"
            "3 - Задача 3\n"
            "4 - Задача 4\n"
            "5 - Задача 5\n"

        )
    )
    n = input("Введите номер задачи -> ")
    
    if n == "0":
        break
    elif n == "1":
        task_1()
    elif n == "2":
        task_2()
    elif n == "3":
        task_3()
    elif n == "4":
        task_4()
    elif n == "5":
        task_5()
    else:
        print("Нет такой задачи")