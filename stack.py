class stack:


    def __init__(self):
        self.arr = []

    def is_empty(self):
        self.arr == []

    def push(self,data):
        self.arr.append(data)

    def pop(self):
        return self.arr.pop()


s = stack()
while True:
    print('push "Enter value"')
    print('pop')
    print('quit')
    do = input("hey boi do you like stack " ).split()
    operation = do[0]
    if operation == 'push':
        s.push(int(do[1]))
    elif operation == 'pop':
        if s.is_empty():
            print('Stack is empty.')
        else:
            print('Popped value: ', s.pop())
    elif operation == 'quit':
        break