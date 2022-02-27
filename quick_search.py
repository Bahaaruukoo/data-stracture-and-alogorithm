class quick_search:
    def __init__(self):
        pass
    def swap(self, a, b, arr):
        if a!=b:
            tmp = arr[a]
            arr[a] = arr[b]
            arr[b] = tmp
    def quick_lumuto(self, lst, start, end):
        if(start < end):
            index = self.lumuto_partition(lst,start, end)
            self.quick_lumuto(lst, start,index-1)
            self.quick_lumuto(lst, index+1, end)
    def lumuto_partition(self, lst, start, end):
        pivot = lst[end]
        i = start - 1
        j = start - 1
        while( j < end):
            j += 1
            #if lst[j] >= pivot:

            if lst[j] < pivot:
                 i += 1
                 print(i, j)
                 self.swap(i,j, lst)
        i += 1
        #if(i < end):
        self.swap(i,end,lst)
        return i
    def Hoare(self, lst, start_index, end_index):
        pivot_index = start_index
        pivot = lst[start_index]
        while start_index < end_index:
            while start_index < len(lst) and lst[start_index] <= pivot :
                start_index += 1
            while lst[end_index] > pivot:
                end_index -= 1
            if(start_index < end_index):
                self.swap(start_index, end_index, lst)

        self.swap(end_index, pivot_index, lst)
        return end_index

    def sort_quick(self, str, start, end):
        if start < end:
            partition_index = self.Hoare(str, start, end)
            #if partition_index - 1 >= 0:
            self.sort_quick(str, start, partition_index-1)
            #if partition_index +1 < end:
            self.sort_quick(str, partition_index + 1, end)
            return str

    def partition(self, elements, start, end):
        pivot_index = start
        pivot = elements[pivot_index]

        while start < end:
            while start < len(elements) and elements[start] <= pivot:
                start+=1
#                print('Start : ', start, elements[start])
            while elements[end] > pivot:
                end-= 1
 #               print('End: ', end, elements[end])
            if start < end:
 #               print('Swaping:' , start, end)
                self.swap(start, end, elements)

#        print('Swaping again:' , start, end)
        self.swap(pivot_index, end, elements)

        return end
if __name__ == '__main__':
    #lst = [11,9,29,7,2,15,28]
    lst = [2,7,1,8,6,3,5,4]
    sort = quick_search()
    #result = sort.Hoare(lst, 0, len(lst) - 1)
    #result2 = sort.sort_quick(lst, 0, len(lst) - 1)

    ii = sort.lumuto_partition(lst, 0, len(lst) - 1)
    print(ii)
   # print(result2)
    print(lst)
    sort.quick_lumuto(lst, 0, len(lst)- 1)
    print('Lumuto: ', lst)
    #print(lst.insert(2,lst.pop(6)))
