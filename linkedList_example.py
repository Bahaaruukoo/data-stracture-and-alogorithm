class Node:
    def __init__(self, data=None, next=None, past = None):
        self.data = data
        self.next = next
        self.past = past

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def print(self):
        llstr = ''
        if self.head == None:
            print('empty list')
        itr = self.head
        while itr:
            #print(itr.data)
            #llstr = llstr + itr.data + '-->' if(itr.next) else str(itr.data)
            llstr += str(itr.data)+' --> ' #if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)

    def insert_values(self, data_list):
        leng = len(data_list)
        #if self.head is None:
        self.head = self.tail = Node(data_list[leng-1], None, None)
        temp = self.head
        newlen = leng - 2
        while newlen >= 0:

           # self.head = Node(data_list[newlen], self.head, None)
           node = Node(data_list[newlen], self.head, None)
           temp.past = node
           self.head = node
           temp = self.head
           newlen = newlen - 1
        return
    def test(self):
        st = ''
        itr = self.tail
        #print(itr.past.data)
        while itr:
            st = st +str(itr.data) + ' --> '
            itr = itr.past
        print(st)
        return
    def get_length(self):
        if self.head is None:
            return 0
        count = 0
        itr = self.head
        while itr:
            count +=1
            itr = itr.next
        return count

    def insert_at_begining(self, data):
        self.head = Node(data, self.head)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, self.head)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def insert_at(self, index, data):
        if index == 0:
            self.insert_at_begining(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count is index - 1:
                itr.next = Node(data, itr.next)
                return
            itr = itr.next
            count += 1

    def remove_at(self, index):
        if index == 0:
            self.head = self.head.next
            return
        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
            count += 1
            itr = itr.next

if 1 == 1: #if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
 #   ll.insert_at_begining("lemon")
  #  ll.insert_at_end("pp")
  #  ll.insert_at(0,"blueberry")
  #  ll.remove_at(9)
    ll.print()
    print('')
    ll.test()
    print(ll.get_length())
    ll.insert_values([45,7,12,567,99])
  #  ll.insert_at_begining(12)
   # ll.insert_at_end(67)
    ll.print()
    #ll.test()
