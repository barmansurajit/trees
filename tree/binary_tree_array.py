class Tree:

    def __init__(self, n):
        self.tree_arr = [None] * n

    def root(self, key):
        if self.tree_arr[0] is not None:
            print(f"Tree already has a root {self.tree_arr[0]}")
        else:
            self.tree_arr[0] = key

    def set_left(self, key, parent):
        if self.tree_arr[parent] is None:
            print(f"Cannot set child at {parent * 2 + 1}, since no parent found")
        else:
            self.tree_arr[parent * 2 + 1] = key

    def set_right(self, key, parent):
        if self.tree_arr[parent] is None:
            print(f"Cannot set child at {parent * 2 + 2}, since no parent found")
        else:
            self.tree_arr[parent * 2 + 2] = key

    def print_tree(self):
        for i in range(10):
            if self.tree_arr[i] is not None:
                print(self.tree_arr[i], end="")
            else:
                print("-", end="")
        print()


t = Tree(10)
t.root('A')
# t.set_left('B', 0)
t.set_right('C', 0)
t.set_left('D', 1)
t.set_right('E', 1)
t.set_right('F', 2)
t.print_tree()
