class Node:
    def __init__(self, key: int):
        self.key = key
        self.parent = None
        self.child = None
        self.left = None
        self.right = None
        self.degree = 0
        self.mark = False


class FibonacciHeap:
    def __init__(self):
        self.min = None
        self.n = 0

    def __insert(self, x: Node, y: Node) -> None:
        x.left = y
        x.right = y.right
        y.right = x
        x.right.left = x

    def __cut(self, x: Node, y: Node) -> None:
        if x.right == x:
            y.child = None
        else:
            y.child = x.right
            x.right.left = x.left
            x.left.right = x.right
        y.degree -= 1
        self.__insert(x, self.min)
        x.parent = None
        x.mark = False

    def __cascading_cut(self, y: Node) -> None:
        z = y.parent
        if z is not None:
            if y.mark is False:
                y.mark = True
            else:
                self.__cut(y, z)
                self.__cascading_cut(z)

    def __link(self, y: Node, x: Node) -> None:
        y.left.right = y.right
        y.right.left = y.left
        y.parent = x
        if x.child is None:
            x.child = y
            y.right = y
            y.left = y
        else:
            self.__insert(y, x.child)
        x.degree += 1
        y.mark = False

    def __consolidate(self) -> None:
        A = [None] * self.n
        w = self.min
        while True:
            d = w.degree
            x = w
            while A[d] is not None:
                y = A[d]
                if x.key > y.key:
                    x, y = y, x
                self.__link(y, x)
                A[d] = None
                d += 1
            A[d] = x
            w = w.right
            if w == self.min:
                break
        self.min = None
        for i in range(self.n):
            if A[i] is not None:
                if self.min is None:
                    self.min = A[i]
                else:
                    self.__insert(A[i], self.min)
                    if A[i].key < self.min.key:
                        self.min = A[i]

    def insert(self, x: Node) -> None:
        if self.min is None:
            self.min = x
        else:
            self.__insert(x, self.min)
            if x.key < self.min.key:
                self.min = x
        self.n += 1

    def extract_min(self) -> Node:
        z = self.min
        if z is not None:
            if z.child is not None:
                child = z.child
                while True:
                    child.parent = None
                    child = child.right
                    if child == z.child:
                        break
            if z.right == z:
                self.min = None
            else:
                self.min = z.right
                self.__consolidate()
            self.n -= 1
        return z

    def decrease_key(self, x: Node, k: int) -> None:
        if k > x.key:
            return
        x.key = k
        y = x.parent
        if y is not None and x.key < y.key:
            self.__cut(x, y)
            self.__cascading_cut(y)
        if x.key < self.min.key:
            self.min = x
