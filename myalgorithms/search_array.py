from random import shuffle


class SearchArray:
    def __init__(self, iter=None):
        if iter is not None:
            self.tree = list(iter)
            self.tree.sort()
        else:
            self.tree = list()

    def search(self, value):
        return self.__binary(self.tree, value, 0, len(self.tree) - 1)

    def __binary(self, l, value, left, right):
        if right < left:
            return -1

        mid = left + (right - left) // 2

        if l[mid] == value:
            return mid
        elif l[mid] < value:
            return self.__binary(l, value, mid + 1, right)
        else:
            return self.__binary(l, value, left, mid - 1)

    def min(self):
        return self.tree[0]

    def max(self):
        return self.tree[-1]

    def predecessor(self, value):
        search_value = self.search(value)
        if search_value == 0:
            return None
        return search_value - 1

    def successor(self, value):
        search_value = self.search(value)
        if search_value == len(self.tree) - 1:
            return None
        return search_value + 1

    def output_sorted(self):
        return self.tree

    def select(self, idx):
        return self.tree[idx]

    def rank(self, k):
        return self.__binary_rank(self.tree, k, 0, len(self.tree) - 1)

    def __binary_rank(self, l, value, left, right):
        if right < left:
            if left == 0 or left == len(self.tree):
                return None
            return right
        else:
            mid = left + (right - left) // 2

            if l[mid] == value:
                return mid
            elif l[mid] < value:
                return self.__binary_rank(l, value, mid + 1, right)
            else:
                return self.__binary_rank(l, value, left, mid - 1)


l = [-12, -2, -1, 1, 1, 10, 13, 23, 34, 34, 65, 98, 101, 101]

# print(binary(l, 101, 0, len(l) - 1))
# shuffle(l)
#
t = SearchArray(l)
# print(t.search(101))
print(t.rank(99))
