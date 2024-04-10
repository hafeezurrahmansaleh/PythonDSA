import time
from collections import deque
import threading


class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.appendleft(item)

    def dequeue(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0

    def __str__(self):
        return str(self.items)


q = Queue()


def place_order(orders):
    global q
    for order in orders:
        q.enqueue(order)
        print(f'Placed order: {order}')
        time.sleep(.5)


def serve_order():
    while True:
        if q.is_empty():
            break
        print(f'Served order: {q.dequeue()}')
        time.sleep(.5)


if __name__ == '__main__':
    queue = Queue()
    queue.enqueue('Saleh')
    queue.enqueue('Vijay')
    queue.enqueue('Pranjal')
    print(queue)
    print(queue.dequeue())

    print('Restaurant Opened')
    t = time.time()
    orders = ['pizza', 'samosa', 'pasta', 'biryani', 'burger']
    # place_order(orders)
    # serve_order()

    thread1 = threading.Thread(target=place_order, args=(orders,))
    thread2 = threading.Thread(target=serve_order)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    t1 = time.time() - t
    print(f'Total time took: {t1:.2f} seconds')
    print('Restaurant closed')
