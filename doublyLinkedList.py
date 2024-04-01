class Node:
    def __init__(self, data=None, prev_node=None, next_node=None):
        self.data = data
        self.prev_node = prev_node
        self.next_node = next_node


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert_at_beginning(self, data):
        self.head = Node(data=data, prev_node=None, next_node=self.head)
        return

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return
        itr = self.head
        while itr.next_node:
            itr = itr.next_node
        itr.next_node = Node(data, itr, None)

    def get_length(self):
        itr = self.head
        count = 0
        while itr:
            count += 1
            itr = itr.next_node
        return count

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception('Invalid index provided')
        if index == 0:
            self.insert_at_beginning(data)
            return
        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                new_node = Node(data, itr, itr.next_node)
                itr.next_node.prev_node = new_node
                itr.next_node = new_node
            count += 1
            itr = itr.next_node

    def delete_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception('Invalid index provided')
        if index == 0:
            self.head.next_node.prev_node = None
            self.head = self.head.next_node
            return
        itr = self.head
        count = 0
        while itr.next_node:
            if count == index - 1:
                itr.next_node.next_node.prev_node = itr
                itr.next_node = itr.next_node.next_node
            count += 1
            itr = itr.next_node

    def insert_after_value(self, data_after, data_to_insert):
        itr = self.head
        found = 0
        while itr:
            if itr.data == data_after:
                new_node = Node(data_to_insert, itr, itr.next_node)
                itr.next_node.prev_node = new_node
                itr.next_node = new_node

                found = 1
                break
            itr = itr.next_node
        if found:
            print('Data inserted')
        else:
            print('Data not found')

    def delete_by_value(self, data):
        itr = self.head
        found = 0
        while itr:
            if itr.next_node.data == data:
                itr.next_node.next_node.prev_node = itr
                itr.next_node = itr.next_node.next_node
                found = 1
                break
            itr = itr.next_node
        if found:
            print('Data deleted')
        else:
            print('Data not found')

    # Remove first node that contains data

    def print_forward(self):
        itr = self.head
        while itr:
            print(itr.data, end='-->')
            itr = itr.next_node

    def print_backward(self):
        itr = self.head
        last = itr
        while itr:
            last = itr
            itr = itr.next_node
        while last:
            print(last.data, end='<--')
            last = last.prev_node


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_beginning('Dhaka')
    ll.insert_at_beginning('Barishal')
    ll.insert_at_beginning('Khulna')
    ll.insert_at_end('Rajshahi')
    ll.print_forward()
    print(f'\nLength is: {ll.get_length()}')
    print('\n')
    ll.insert_at_end('Chittagong')
    ll.print_forward()
    print(f'\nLength is: {ll.get_length()}')
    ll.insert_at(0, 'Sylhet')
    ll.print_forward()
    print(f'\nLength is: {ll.get_length()}')
    ll.insert_at(2, 'Rangpur')
    ll.print_forward()
    print(f'\nLength is: {ll.get_length()}')

    ll.delete_at(5)
    ll.print_forward()
    print(f'\nLength is: {ll.get_length()}')
    ll.delete_at(0)
    ll.print_forward()
    print(f'\nLength is: {ll.get_length()}')

    ll.insert_after_value('Barishal', 'Cumilla')
    ll.print_forward()
    print(f'\nLength is: {ll.get_length()}')

    ll.delete_by_value('Dhaka')
    ll.print_forward()
    print(f'\nLength is: {ll.get_length()}')

    ll.print_backward()
