from math import ceil, pow


class Heap:

    def __init__(self):
        self.heap = list()
        self.heap_size = -1

    def insert(self, value):
        self.heap.append(value)
        self.heap_size += 1
        self.checkviolations(self.heap_size)
        print("inserted ", value)

    def checkviolations(self, child_position):
        if child_position == 0:
            return
        child_value = self.heap[child_position]
        parent_position = ceil(child_position / 2 - 1)
        parent_value = self.heap[parent_position]
        if parent_value < child_value:
            self.swap(child_position, parent_position)
            self.checkviolations(parent_position)

    def swap(self, child_position, parent_position):
        child_value = self.heap[child_position]
        parent_value = self.heap[parent_position]
        self.heap[child_position] = parent_value
        self.heap[parent_position] = child_value
        # print("items swaped ", child_value, "and ", parent_value)

    def __str__(self):
        str(self.heap)

    def print_heap(self):
        item_number_in_row = 1
        row = 0
        place = 0
        while place <= self.heap_size:
            for i in range(0, item_number_in_row):
                if i + place <= self.heap_size:
                    print(self.heap[place + i], end=' ')
            print("\n")
            place += item_number_in_row
            row += 1
            item_number_in_row = int(pow(2, row))

    def pool(self):
        max = self.heap[0]
        self.swap(0, self.heap_size)
        del self.heap[self.heap_size]
        self.heap_size -= 1
        self.checkviolations_down(0)
        return max

    def checkviolations_down(self, parent_position):
        child1_position = 2 * parent_position + 1
        child2_position = 2 * parent_position + 2
        largest_index = child1_position
        if child2_position <= self.heap_size:
            if self.heap[child1_position] < self.heap[child2_position]:
                largest_index = child2_position
        if child1_position > self.heap_size:
            return
        elif self.heap[parent_position] < self.heap[largest_index]:
            self.swap(parent_position, largest_index)
            self.checkviolations_down(largest_index)

    def get_max(self):
        return self.heap[0]

    def heap_sort(self):
        for i in range (0,self.heap_size):
            print("the max value is ", self.pool())


if __name__=="__main__":
    h = Heap()
    h.insert(5)
    h.insert(6)
    h.insert(4)
    h.insert(0)
    h.insert(10)
    h.insert(2)
    for i in range(10, 20):
        h.insert(i)
    h.print_heap()
    for i in range(3):
        max_heap = h.pool()
        print("max heap is, ", max_heap)
        h.print_heap()
    h.heap_sort()
