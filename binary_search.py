class binary_serch:
    def __init__(self, lst):
        self.lst = lst

    def search(self, find):
        initial_index = 0
        last_index = len(self.lst) - 1
        mid_index = 0
        while initial_index <= last_index:
            mid_index = (initial_index + last_index) // 2
            if find == self.lst[mid_index]:
                return mid_index
            elif find < self.lst[mid_index]:
                last_index = mid_index - 1
            else:
                initial_index = mid_index + 1
        return None

    def binary_search_recursive(self, find, initial_index, final_index):
        ll = []
        if initial_index > final_index:# or final_index <= initial_index:
            return -1
        mid_index = (initial_index + final_index) // 2
        if self.lst[mid_index] == find:
            i = mid_index - 1
            while self.lst[i] == find and i >= initial_index:
                ll.append(i)
                i = i-1
            ll.append(mid_index)
            j = mid_index + 1
            while self.lst[j] == find and j <= final_index:
                ll.append(j)
                j = j+1
            return ll
        if find < self.lst[mid_index]:
            final_index = mid_index - 1
        else:
            initial_index = mid_index + 1
        return self.binary_search_recursive(find,initial_index,final_index)


if __name__ == '__main__':
    numbers_list = numbers = [1,4,6,9,11,15,15,15,17,21,34,34,56] #[12, 15, 17, 19, 21, 24, 45, 67]
    number_to_find = 15
    lst = binary_serch(numbers_list)
    index = lst.search(number_to_find)
    indexR = lst.binary_search_recursive(number_to_find, 0, len(numbers_list)-1)
    print(f"Number found at index {index} using binary search")
    print(  indexR)
    print(len(numbers_list))
