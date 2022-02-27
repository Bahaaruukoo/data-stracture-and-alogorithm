class Node:
    def __init__(self, data):
        self.data = data
        self.child = []
        self.parent = None

    def add_child(self, child):
        self.child.append(child)
        child.parent = self

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_campany(self, option):
        if option == 'Name': index = 0
        elif option == 'Title': index = 1
        elif option == '': index = None
        else: return "wrong option"
        level = self.get_level()
        space = ''
        if level:
            space = ' ' * level * 3 + '|__'

        if index is None:
            print(space + self.data[0] + ' (' + self.data[1] + ')')
        else:
            print(space + self.data[index])
        if self.child:
            for child in self.child:
                child.print_campany(option)

    def print_levels(self, option):
        space = ''
        level = self.get_level()

        if level <= option:
            space = ' ' * level * 3 + '|__'
            print(space + self.data[0] + ' (' + self.data[1] + ')')

            if self.child:
                for child in self.child:
                    child.print_levels(option)

Ceo = Node(['Nilupi','CEO'])
Chinmay = Node(['Chinmay','CTO'])
Gels = Node(['Gels', 'HR Head'])

Vishwa = Node(['Vishwa','Infrastructure Head'])
Dhaval = Node(['Dhaval','Cloud Managere'])
Abhijit = Node(['Abhijit','App Manager'])
Aamir = Node(['Aamir','application Head'])
Peter = Node(['Peter','Recruitment Manager'])
Waqas = Node(['Waqas','Policy Manager'])

Ceo.add_child(Chinmay)
Ceo.add_child(Gels)
Chinmay.add_child(Vishwa)
Chinmay.add_child(Aamir)
Vishwa.add_child(Dhaval)
Vishwa.add_child(Abhijit)
Gels.add_child(Peter)
Gels.add_child(Waqas)
#Ceo.print_campany('Title')
Ceo.print_levels(1)
Ceo.print_levels(2)
Ceo.print_levels(3)
