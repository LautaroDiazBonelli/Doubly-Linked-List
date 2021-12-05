
class Nodo:
    def __init__(self, next=None, prev=None, value=None):
        self.next = next
        self.prev = prev
        self.value = value


class doubleList(object):
    def __init__(self):
        self.prim = Nodo()
        self.ult = Nodo(prev=self.prim)
        self.prim.next = self.ult
        self.size = 0

    def pushBack(self, value):  # O(1)
        aux = Nodo(self.ult, self.ult.prev, value)
        self.ult.prev.next = aux
        self.ult.prev = aux
        self.size += 1

    def pushFront(self, value):  # O(1)
        aux = Nodo(self.prim.next, self.prim, value)
        self.prim.next.prev = aux
        self.prim.next = aux
        self.size += 1

    # def popFront(self):
    #     aux = self.prim.next.next
    #     self.prim=aux
    #     aux.prev= self.prim
    #     self.size-=1
    #
    # def popBack(self):
    #     aux = self.ult.prev.prev
    #     self.ult=aux
    #     aux.next= self.ult
    #     self.size-=1

    def __iter__(self):
        if self.size > 0:
            self.it = self.prim.next
            return self
        else:
            raise StopIteration

    def __next__(self):
        if self.it == self.ult:
            raise StopIteration
        else:
            aux = self.it
            self.it = self.it.next
        return aux.value

    def __getitem__(self, item):
        i = 0
        nd = self.prim.next
        while i < item and nd != self.ult:
            nd = nd.next
            i += 1
        return nd.value

    def __repr__(self):  # O(n)
        aux = self.prim.next
        res = "["
        while aux != self.ult.prev and aux != self.ult:
            res += f"{aux.value}, "
            aux = aux.next
        res += f"{self.ult.prev.value}]"
        return res

    def __len__(self):
        return self.size

    def erase(self, pos):
        i = 0
        nd = self.prim.next
        while i < pos and nd != self.ult:
            nd = nd.next
            i += 1
        if nd != self.ult:
            nd.prev.next = nd.next
            nd.next.prev = nd.prev
            self.size -= 1

    def __reversed__(self):
        newList = doubleList()
        nd = self.prim.next
        while nd != self.ult:
            newList.pushBack(nd)
            nd = nd.next
        return newList

    def __contains__(self, item):
        nd = self.prim.next
        res = False
        while nd != self.ult and not res:
            if nd.value == item:
                res = True
            nd = nd.next
        return res

    def __delitem__(self, key):
        self.erase(key)

    def empty(self):
        i = self.size - 1
        nd = self.ult.prev
        while nd != self.prim:
            self.erase(i)
            nd = nd.prev
            i -= 1
        self.size = 0
