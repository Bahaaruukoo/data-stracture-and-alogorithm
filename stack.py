from _collections import deque
class Stack():
    def __init__(self):
        self.container = deque()

    def push(self, data):
        self.container.append(data)

    def pop(self):
        return self.container.pop()

    def size(self):
        return  len(self.container)

    def peek(self):
        return self.container[-1]
    def reverse_string(self, data):
        str =''
        for char in data:
            self.push(char)

        while len(self.container):
            str = str + self.container.pop()

        return str

st = Stack()
rev = st.reverse_string("We will conquere COVID-19")
#should return "91-DIVOC ereuqnoc lliw eW"
print(rev)

def is_match(ch1, ch2):
    match_dict = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    return match_dict[ch1] == ch2


def is_balanced(s):
    stack = Stack()
    for ch in s:
        if ch=='(' or ch=='{' or ch == '[':
            stack.push(ch)
        if ch==')' or ch=='}' or ch == ']':
            if stack.size()==0:
                return False
            if not is_match(ch,stack.pop()):
                return False

    return stack.size()==0


if __name__ == '__main__':
    print(is_balanced("({a+b})"))
    print(is_balanced("))((a+b}{"))
    print(is_balanced("((a+b))"))
    print(is_balanced("((a+g))"))
    print(is_balanced("())"))
    print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))
