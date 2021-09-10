import random
from circular_queue import CircularQueue
from constants import MAX_BUFFER_SIZE


class BufferOutput:

    def __init__(self, titles):
        self.titles = titles
        self.len_titles = len(titles)
        self.output_items = []
        self.deliver = " "

    def buffer_manage(self):
        if not self.titles:
            return 'There are no titles'

        obj = CircularQueue(MAX_BUFFER_SIZE)
        index_title = 0
        queue = random.randint(1, len(self.titles)) 
        while queue > 0:
            if obj.insert_queue(self.titles[index_title]):
                self.output_items = obj.return_queue()

                obj.remove_queue()

                queue -= 1
                continue

            index_title += 1
            if index_title == len(self.titles):
                index_title = 0

        return self.output_items
