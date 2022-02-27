from _collections import deque
import time
import threading

class Que:
    def __init__(self):
        self.container = deque()

    def enqueue(self, data):
        print('i am here first')
        for elem in data:
            time.sleep(1)
            self.container.appendleft(elem)
            print('Appended....')

    def dequeue(self):
        print('i am here')
        while (len(self.container)):
            time.sleep(2)
            print(self.container.pop())

    def size(self):
        return len(self.container)

dq = Que()
data = ('pizza','samosa','pasta','biryani','burger')

t1 = threading.Thread(target=dq.enqueue, args=(data,))
t2 = threading.Thread(target=dq.dequeue, args=())

t1.start()
time.sleep(1)
t2.start()

t1.join()
t2.join()

#dq.enqueue(data)
print(dq.size())
#print(dq.dequeue())


