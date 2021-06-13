"""
Given a list of iterators, 
implement a FlattenedIterator class which incrementally iterates over the integers from all the iterators in an interleaved fashion. 

Example:
    Iterators[0] = [1,2,3]
    Iterators[1] = [4,5]
    Iterators[2] = [6,7,8]

    FlattenedIterator = [1, 4, 6, 2, 5, 7, 3, 8]

An iterator implements the next() and hasNext() interface. 
You're free to use them, and you will implement them on the FlattenedIterator class.
You're free to initialize FlattenedIterator with any data structure of your choice for the iterators. 
"""


class FlattenedIterator:
    def __init__(self, subiterators):
        self.curr_index = 0
        self.subiterators = []
        for iter in subiterators:
            if iter.hasNext():
                self.subiterators.append(iter)

    def removeCurrIterator(self):
        self.subiterators.pop(self.curr_index)

    def moveToNextIdex(self):
        curr_index = self.curr_index

        if not self.subiterators[curr_index].hasNext():
            # check if current subiterator is still valid
            self.removeCurrIterator()
        else:
            curr_index = self.curr_index + 1

        # check if is valid idx
        if curr_index <= len(self.subiterators) - 1:
            self.curr_index = curr_index
        else:
            self.curr_index = 0

    def hasNext(self):
        if (self.subiterators):
            return True

        return False

    def next(self):

        if self.hasNext():
            nxt = self.subiterators[self.curr_index].next()
            self.moveToNextIdex()
            return nxt


# # # # # <----------------------------------------- Tests ------------------------------------------>

class ListIterator:
    def __init__(self, items):
        self.items = list(items)

    def hasNext(self):
        return bool(self.items)

    def values(self):
        return (self.items)

    def next(self):
        if self.hasNext():
            return self.items.pop(0)
        else:
            raise Exception()


A = ListIterator([1, 2, 3])
B = ListIterator([4, 5])
C = ListIterator([6, 7, 8])
# it = FlattenedIterator([A, B, C])

# assert(it.hasNext() and it.next() == 1 and
#        it.hasNext() and it.next() == 4 and
#        it.hasNext() and it.next() == 6 and
#        it.hasNext() and it.next() == 2 and
#        it.hasNext() and it.next() == 5 and
#        it.hasNext() and it.next() == 7 and
#        it.hasNext() and it.next() == 3 and
#        it.hasNext() and it.next() == 8 and
#        not it.hasNext())

# A = ListIterator([])
# B = ListIterator([])
# C = ListIterator([])

# it2 = FlattenedIterator([A, B, C])

# print(it2.hasNext(), it2.next())
# print(it2.hasNext(), it2.next())
# print(it2.hasNext(), it2.next())
# print(it2.hasNext(), it2.next())
# print(it2.hasNext(), it2.next())
# print(it2.hasNext(), it2.next())
# print(it2.hasNext(), it2.next())
# print(it2.hasNext(), it2.next())
# print(it2.hasNext(), it2.next())
