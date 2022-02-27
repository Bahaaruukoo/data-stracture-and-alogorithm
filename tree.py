class treeNode:
    def __init__(self, data):
        self.data = data
        self.child = []
        self.parent = None

    def addChild(self, child):
        child.parent = self
        self.child.append(child)
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def treePrint(self, lev):
        if self.parent:
            space =' ' * lev *2 + '|__'
        else: space = ''
        print(space + self.data)
        if self.child:
            space =' '
            lev = lev + 1
            space = (" " * lev + "|__")

            for ch in self.child:
                ch.treePrint( lev)

root = treeNode('Electronics')

laptop = treeNode('laptop')
mobile = treeNode('mobile')
tv = treeNode('tv')

mobile.addChild(treeNode('sumsung'))
mobile.addChild(treeNode('iPhone'))
mobile.addChild(treeNode('huawei'))

tv.addChild(treeNode('LG'))
tv.addChild(treeNode('MeWe'))
tv.addChild(treeNode('Sony'))

laptop.addChild(treeNode("Thinkpad"))
laptop.addChild(treeNode("toshiba"))

root.addChild(laptop)
root.addChild(mobile)
root.addChild(tv)

root.treePrint(0)
print(tv.get_level())
