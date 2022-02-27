class binary_tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    def add_child(self, child):
        if child == self.data:
            return
        if child < self.data:
            if self.left:
                self.left.add_child(child)
            else:
                self.left = binary_tree(child)
        else:
            if self.right:
                self.right.add_child(child)
            else:
                self.right = binary_tree(child)
    def make_tree(self, arr):
        for data in arr[1:]:
            self.add_child(data)

    def mid_traversal(self):
        element = []
        if self.left:
            element += self.left.mid_traversal()
        element.append(self.data)
        if self.right:
            element += self.right.mid_traversal()
        return element
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

    def delete_with_max(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete_with_max(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete_with_max(val)
        else:
            if self.right is None and self.left is None:
                return None
            elif self.right is None:
                return self.left
            elif self.left is None:
                return self.right
            else:
                max = self.left.find_max()
                self.data = max
                self.left = self.left.delete_with_max(max)
        return self
    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)

        else:
            if self.left is None and self.right is None:
                return None
            elif self.right is None:
                return self.left
            elif self.left is None:
                return self.right
            else:
                min = self.right.find_min()
                self.data = min
                self.right = self.right.delete(min)
        return self
    def check(self):
        return self.data
arr = [44,54,33,88,12,40, 42,29,80, 29, 50,60]
num_tree = binary_tree(arr[0])
num_tree.make_tree(arr)
print(num_tree.mid_traversal())
#print(num_tree.find_min())
#num_tree.delete(44)
#print(num_tree.mid_traversal())
num_tree.delete_with_max(44)
print(num_tree.mid_traversal())
