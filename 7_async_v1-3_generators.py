# Round Robin
from time import sleep 
queue = []  # очередь задач

def print_nums():
    num = 0
    while True:
        print(num)
        num += 1
        yield # from asyncio.sleep(1)     # асинхронная функция задержки, на 1 сек


def print_time():
    count = 0
    while True:
        if count % 3 == 0:
            print('{} seconds have passed'.format(count))
        count += 1
        yield # from asyncio.sleep(1)


def main():
    while True:
        g = queue.pop(0)
        next(g)
        queue.append(g)
        sleep(1)



if __name__ == '__main__':
    g1 = print_nums()
    queue.append(g1)
    g2 = print_time()
    queue.append(g2)
    main()