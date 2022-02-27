class merge_sort:
    def __init__(self):
        pass
    def merging_lst(self, lst,  key, descending=False):
        if len(lst) <= 1:
            return

        mid= len(lst)//2

        left = lst[:mid]
        right = lst[mid:]

        self.merging_lst(left,  key, descending)
        self.merging_lst(right, key,descending)

        self.merge(left, right, lst, key, descending)

    def merge(self, a, b, lst, key, descending):
        len_a = len(a)
        len_b = len(b)

        i = j = k = 0
        while i < len_a and j < len_b:
            if descending is True:
                if a[i][key] >= b[j][key]:
                    lst[k] = a[i]
                    i += 1
                else:
                    lst[k] = b[j]
                    j += 1
                k += 1
            else:
                if a[i][key] <= b[j][key]:
                    lst[k] = a[i]
                    i += 1
                else:
                    lst[k] = b[j]
                    j += 1
                k += 1
        while i < len_a:
            lst[k] = a[i]
            i += 1
            k += 1
        while j < len_b:
            lst[k] = b[j]
            j += 1
            k += 1


if __name__ == '__main__':
    sort = merge_sort()
    lst = [2, 7, 1, 8, 6, 3, 5, 4]
    lst1 = [6,4]
    lst2 = [2, 7, 1, 8, 6, 3, 5, 4, 11, 9,0]
    #sort.merging_lst(lst)
    print(lst)
    elements = [
        { 'name': 'vedanth',   'age': 17, 'time_hours': 1},
        { 'name': 'rajab', 'age': 12,  'time_hours': 3},
        { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
        { 'name': 'chinmay',  'age': 24,  'time_hours': 1.5},
        { 'name': 'chinmayw',  'age': 20,  'time_hours': 1.6},
    ]
    sort.merging_lst(elements, 'age', descending=True)
    print(elements)
