class binary_tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, element):
        if element == self.data:
            return
        if element < self.data:
            if self.left:
                self.left.add_child(element)
            else:
                self.left = binary_tree(element)

        else:
            if self.right:
                self.right.add_child(element)
            else:
                self.right = binary_tree(element)

    def in_order_travers(self):
        element = []
        if self.left:
            element += self.left.in_order_travers()

        element.append(self.data)

        if self.right:
            element += self.right.in_order_travers()
        return element

    def post_order(self):
        element = []
        if self.left:
            element += self.left.post_order()
        if self.right:
            element += self.right.post_order()
        element.append(self.data)
        return element

    def pre_order(self):
        element = []
        element.append(self.data)
        if self.left:
            element += self.left.pre_order()
        if self.right:
            element += self.right.pre_order()
        return element

    def search(self, element):
        if self.data == element:
            return True
        if element < self.data:
            if self.left:
                return self.left.search(element)
            else: return False
        if element > self.data:
            if self.right:
                return self.right.search(element)
            else: return False

    def find_max(self):
        if self.right:
            return self.right.find_max()
        else:
            return self.data
    def find_min(self):
        if self.left:
            return self.left.find_min()
        else:
            return self.data
    def total_sum(self):
        sum = 0
        if self.left:
            sum += self.left.total_sum()
        sum += self.data
        if self.right:
            sum += self.right.total_sum()
        return  sum
def make_tree(data):
    root = binary_tree(data[0])

    for i in range (1, len(data)):
        root.add_child(data[i])
    return root

if __name__ == '__main__':

    numbers_tree = make_tree([17, 4, 1, 20, 9, 23, 18, 34])
    print("In order traversal gives this sorted list:",numbers_tree.in_order_travers())

    countries = ["India","Pakistan","Germany", "USA","China","India","UK","USA"]
    country_tree = make_tree(countries)
    print("In order traversal gives this sorted list:",country_tree.in_order_travers())
    print(country_tree.search("UK"))

    print(numbers_tree.find_max())
    print(numbers_tree.find_min())
    print(numbers_tree.total_sum())
    print(numbers_tree.post_order())
    print(numbers_tree.in_order_travers())
    print(numbers_tree.pre_order())
