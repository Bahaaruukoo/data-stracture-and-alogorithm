class selection:
    def __init__(self):
        pass
    def selection_sort(self, lst):
        y = 0
        size = len(lst)
        while y < size:
            min = lst[y]
            for x in range(y+1,size):
                if lst[x] < min:
                    temp = min
                    min = lst[x]
                    lst[x] = temp
            lst[y] = min
            y += 1
    def muli_level_sort(self, lst, order):
        y = 0
        size = len(lst)
        key = order[0]
        secondKey = order[1]
        while y < size:
            min = lst[y]
            min_index = y
            for x in range(y+1,size):
                if lst[x][key] < min[key]:
                    min = lst[x]
                    min_index = x
                if lst[x][key] == min[key]:
                    if lst[x][secondKey] < min[secondKey]:
                        min = lst[x]
                        min_index = x
            temp = lst[y]
            lst[y] = lst[min_index]
            lst[min_index] = temp
            y += 1

if __name__ == '__main__':
    sort = selection()
    lst3 = [
    {'First Name': 'Raj', 'Last Name': 'Nayyar'},
    {'First Name': 'Suraj', 'Last Name': 'Sharma'},
    {'First Name': 'Karan', 'Last Name': 'Kumar'},
    {'First Name': 'Jade', 'Last Name': 'Canary'},
    {'First Name': 'Raj', 'Last Name': 'Thakur'},
    {'First Name': 'Raj', 'Last Name': 'Sharma'},
    {'First Name': 'Kiran', 'Last Name': 'Kamla'},
    {'First Name': 'Armaan', 'Last Name': 'Kumar'},
    {'First Name': 'Jaya', 'Last Name': 'Sharma'},
    {'First Name': 'Ingrid', 'Last Name': 'Galore'},
    {'First Name': 'Jaya', 'Last Name': 'Seth'},
    {'First Name': 'Armaan', 'Last Name': 'Dadra'},
    {'First Name': 'Ingrid', 'Last Name': 'Maverick'},
    {'First Name': 'Aahana', 'Last Name': 'Arora'}
]
    key = ['First Name','Last Name']
    sort.muli_level_sort(lst3,key)
    print(lst3)
