from collections import deque


class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, value):
        self.container.append(value)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

    def __str__(self):
        return str(self.container)


def reverse_string(str):
    stack = Stack()
    for char in str:
        stack.push(char)
    reversed_str = ''
    for i in range(0, stack.size()):
        reversed_str += stack.pop()
    return reversed_str


def is_match(op, cl):
    p_dict = {
        '(': ')',
        '{': '}',
        '[': ']'
    }
    return p_dict[op] == cl


def is_balanced(str):
    stack = Stack()
    for char in str:
        if char in ('(', '{', '['):
            stack.push(char)
        elif stack.is_empty() and char in (')', '}', ']'):
            return False
        elif char in (')', '}', ']'):
            if stack.is_empty():
                return False
            if not is_match(stack.pop(), char):
                return False
    return True


if __name__ == '__main__':
    stack = Stack()
    stack.push('Saleh')
    stack.push('Vijay')
    stack.push('Dip')
    print(stack)
    print(stack.pop())
    print(stack)
    print(stack.size())
    print(stack.peek())
    print(stack)
    print(stack.is_empty())
    print(stack.pop())
    print(stack.pop())
    print(stack.is_empty())

    print("========== Reverse String ===========")
    print(reverse_string("We will conquere COVID-19"))

    print("========== CHeck Balanced String ===========")
    print(is_balanced('({a+b})'))
    print(is_balanced('))((a+b}{'))
    print(is_balanced('((a+b))'))
    print(is_balanced('))'))
    print(is_balanced('[a+b]*(x+2y)*{gg+kk}'))
