class insertion:
    def __init__(self):
        pass
    def insterting(self, lst):
        for i in range(len(lst)):
            anchor = lst.pop(i)
            j = i -1
            while j >= 0 and anchor < lst[j]:
                j = j - 1
            lst.insert(j+1, anchor)
if __name__ == '__main__':

    sort = insertion()
    #lst = [11,9,29,7,2,15,28]
    lst = [2,7,1,8,6,3,5,4]
    tests = [
        [11,9,29,7,2,15,28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]

    for elements in tests:
        sort.insterting(elements)
        print(f'sorted array: {elements}')
    print(lst)
    sort.insterting(lst)
    #result2 = sort.sort_quick(lst, 0, len(lst) - 1)
    print(lst)
