
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

def task_2():
    queue = []
    while True:
        command = input().split()
        
        if command[0] == 'push':
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
        
while True:
    print(
        (
            "0 - Выход\n"
            "1 - Задача 1"
        )
    )
    n = input()
    
    if n == "0":
        break
    elif n == "1":
        task_1()
    else:
        print("Нет такой задачи")