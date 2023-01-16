import hashlib
from typing import List, Iterable, Callable, TypeVar, Generic
from random import randint as r

K = TypeVar('K')


class LinearHashing(Generic[K]):
    def __init__(self, n: int, hash_function: Callable) -> None:
        self.table = [None] * n
        self.hash_function = hash_function

    def insert(self, key: K) -> K | None:
        i = 0
        while i != len(self.table):
            pos = self.hash_function(key)
            if self.table[pos] is None:
                self.table[pos] = key
                return pos
            else:
                i += 1

    def search(self, key: K) -> K | None:
        i = 0
        while i != len(self.table):
            pos = self.hash_function(key)
            if self.table[pos] is None:
                return None
            elif self.table[pos] == key:
                return key
            else:
                i += 1


def isPrime(x):
    count = 0
    for i in range(int(x/2)):
        if x % (i+1) == 0:
            count = count+1
    return count == 1


class RandomHashing(Generic[K]):
    def __init__(self, n: int) -> None:
        self.m = next(i for i in range(n, 2 * n) if isPrime(i))
        self.table = [None] * self.m

    def _get_hash_1(self, key: K) -> int:
        return key % self.m

    def _get_hash_2(self, key: K) -> int:
        return 1 + key % (self.m - r(0, round(self.m * 0.1)))

    def hash_function(self, key: K, i: int) -> int:
        return (self._get_hash_1(key) + i * self._get_hash_2(key)) % self.m

    def insert(self, key: K) -> K | None:
        i = 0
        while i != len(self.table):
            pos = self.hash_function(key, i)
            if self.table[pos] is None:
                self.table[pos] = key
                return pos
            else:
                i += 1

    def search(self, key: K) -> K | None:
        i = 0
        while i != len(self.table):
            pos = self.hash_function(key, i)
            if self.table[pos] is None:
                return None
            elif self.table[pos] == key:
                return key
            else:
                i += 1