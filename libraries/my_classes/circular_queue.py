class CircularQueue:

    def __init__(self, k):
        self.k = k
        self.queue = [None] * k
        self.head = self.tail = -1

    def insert_queue(self, data):

        if (self.tail + 1) % self.k == self.head:
            return True

        elif self.head == -1:
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = data
        else:
            self.tail = (self.tail + 1) % self.k
            self.queue[self.tail] = data

    def remove_queue(self):
        if self.head == -1:
            print("The circular queue is empty\n")

        elif self.head == self.tail:
            self.head = -1
            self.tail = -1
        else:
            self.head = (self.head + 1) % self.k

    def return_queue(self):
        list_1 = []

        if self.head == -1:
            print("No element in the circular queue")

        elif self.tail >= self.head:
            for i in range(self.head, self.tail + 1):
                list_1.append(self.queue[i])
            return list_1
        else:

            for i in range(self.head, self.k):
                list_1.append(self.queue[i])
            for i in range(0, self.tail + 1):
                list_1.append(self.queue[i])
            return list_1
