class SimpleList:
    def __init__(self, items):
        print(f'Init SimpleList, self = {self}, super = {super()}')
        self._items = list(items)

    def add(self, item):
        self._items.append(item)

    def __getitem__(self, index):
        return self._items[index]

    def sort(self):
        self._items.sort()

    def __len__(self):
        return len(self._items)

    # def __repr__(self):
    #     return f"{type(self).__name__}({self._items!r})"

class SortedList(SimpleList):
    def __init__(self, items=()):
        print(f'Init Sorted List, self = {self}, super = {super()}')
        super().__init__(items)
        self.sort()

    def add(self, item):
        super().add(item)
        self.sort()

class IntList(SimpleList):
    def __init__(self, items=()):
        print(f'Init IntList, self = {self}, super = {super()}')
        for x in items: self._validate(x)
        super().__init__(items)

    @staticmethod
    def _validate(x):
        if not isinstance(x, int):
            raise TypeError('IntList only supports integer values.')

    def add(self, item):
        self._validate(item)
        super().add(item)

class SortedIntList(IntList, SortedList):
    pass

SortedIntList()