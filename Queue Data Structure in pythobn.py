class Queue:

    def __init__(self):
        self.arr = []
    def isEmpty(self):
        self.arr == []
    def enqueue(self,data):
        self.arr.append(data)
    def dequeue(self):
        return self.arr.pop(0)

Q = Queue()
while True:
    print("enqueue <value>")
    print("dequeue")
    print("Exit")
    do = input("Do you want Continued....").split()
    opration = do[0]
    if opration == 'enqueue':
        Q.enqueue(int(do[1]))
    elif opration =='dequeue':
        if (Q.isEmpty()):
            print("Queue IS empty")
        else:
            print("Queue is popped",Q.dequeue())
    elif opration =='exit':
        break

