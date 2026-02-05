#!/usr/bin/env python3


class CountedIterator:
    """Iterator that counts how many items have been iterated."""

    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self._count = 0

    def __iter__(self):
        return self

    def __next__(self):
        item = next(self.iterator)   # May raise StopIteration
        self._count += 1
        return item

    def get_count(self):
        return self._count
