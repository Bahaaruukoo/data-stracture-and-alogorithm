class sort():
    def bubble_sort(self, element, key = ''):
        for i in element:
            for j in range(len(element) - 1):
                temp = 0
                if(element[j][key] > element[j+1][key]):
                    temp = element[j][key]
                    element[j][key] = element[j+1][key]
                    element[j+1][key] = temp
        return element

if __name__ == '__main__':
    sorting = sort()

    elements = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
        ]

    sorted = sorting.bubble_sort(elements, key='transaction_amount')
    print(sorted)
