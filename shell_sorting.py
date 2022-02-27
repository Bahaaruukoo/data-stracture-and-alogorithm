class shell:
    def __init__(self):
        pass
    def sort_in_shell(self, lst):
        size = len(lst)
        gap = size//2
        while gap > 0:
            for x in range(0,size,gap):
                for y in range(0,size,gap):
                    if y + gap < size and lst[y] >= lst[y+gap]:
                        if lst[y] == lst[y+gap]:
                            del lst[y]
                            size = len(lst)
                        temp = lst[y]
                        lst[y] = lst[y + gap]
                        lst[y + gap] = temp
            gap = gap // 2

    def sorting(self, lst):
        size = len(lst)
        gap = size//2
        while gap > 0:
            for i in range(size):
                anchor = lst[i]
                j = i
                while j+gap < size and anchor > lst[j+gap]:
                    lst[j] = lst[j+gap]
                    lst[j+gap] = anchor
                    anchor = lst[j+gap]
                    j += gap
            gap = gap //2
    def shell_sort(self, arr):
        size = len(arr)
        gap = size//2

        while gap > 0:
            for i in range(gap,size):
                anchor = arr[i]
                j = i
                while j>=gap and arr[j-gap]>anchor:
                    arr[j] = arr[j-gap]
                    j -= gap
                arr[j] = anchor
            gap = gap // 2


if __name__ == '__main__':
    sort = shell()
    lst = [2, 7, 1, 8, 6, 3, 5, 4]
    sort.sorting(lst)
    print(lst)
    lst1 = [6,4]
    sort.sorting(lst1)
    print(lst1)
    lst2 = [2, 7, 1, 8, 6, 3, 5, 4, 11, 9,0]
    sort.sort_in_shell(lst2)
    print(lst2)
    lst3 = [2, 7, 1, 8, 6, 3, 5, 4, 11, 9,0]
    sort.sort_in_shell(lst3)
    print(lst3)
    lst4 = [2, 1, 5, 7, 2, 0, 5, 1, 2, 9, 5, 8, 3]
    sort.sort_in_shell(lst4)
    print(lst4)

