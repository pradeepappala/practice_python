class Multiset:
    def __init__(self):
        self.multiset = list()

    def add(self, val):
        self.multiset.append(val)
        pass

    def remove(self, val):
        self.multiset.remove(val)
        # removes one occurrence of val from the multiset, if any
        pass

    def __contains__(self, val):
        # returns True when val is in the multiset, else returns False
        return val in self.multiset

    def __len__(self):
        # returns the number of elements in the multiset
        return len(self.multiset)

a = Multiset()
a.add(1)
print(a.__contains__(1))
print(1 in a)
