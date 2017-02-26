# Program: hashtable.py
# Execution: python hashtable.py < data/input.txt
# This hashtable program is modeled after the hashst.py program from
# Princeton. http://introcs.cs.princeton.edu/python/44st/hashst.py.html
# This program supports the public methods size(), isEmpty(), put(), get(),
# delete(), and contains(). It provides an iterator to return the values in the
# table, and a main() method, for testing. 

import sys
import stdio
import re
import stdarray

# Class to represent a key and value object.
class Item:
    def __init__(self, key, value):
        self.key = key
        self.value = value
    def __str__(self):
        return self.key


class Hashtable:

    def __init__(self, size=1031):
        self._size = size
        self._keys = stdarray.create2D(size, 0)
        self._n = 0

    # Return the number of key value pairs in the table.
    def size(self):
        return self._n

    # Check if the table is empty.
    def isEmpty(self):
        return self.size() == 0

    # Return the index computed from the hashcode of the key x.
    def hash(self, x):
        return (hash(x) & 0x7fffffff) % self._size

    # Put the key x in the table. The key x has a value of 1 if
    # its the first time being put, else increment, the value.
    def put(self, x):
        index = self.hash(x)
        item = Item(x, 1)
        for i in range(len(self._keys[index])):
            if self._keys[index][i].key == x:
                self._keys[index][i].value += 1
                return
        self._keys[index] += [item]
        self._n += 1
        self._size = len(self._keys)

    # Return the value associated with the key X.
    def get(self, x):
        index = self.hash(x)
        for i in range(len(self._keys[index])):
            if self._keys[index][i].key == x:
                return self._keys[index][i].value
        return None

    # Remove the key x from the table.
    def delete(self, x):
        index = self.hash(x)
        for i in range(len(self._keys[index])):
            if self._keys[index][i].key == x:
                del self._keys[index][i]
                self._n -= 1
                return

    # Is the key x in the table?
    def contains(self, x):
        return self.get(x) != None

    # Return an iterator containing all the key and value pairs.
    def __iter__(self):
        items = []
        for i in range(len(self._keys)):
            items += self._keys[i]
        return iter(items)


def main():
    hashtable = Hashtable()
    while not stdio.isEmpty():
        a = stdio.readString().lower()
        hashtable.put(re.sub(r'[^\w\s]','',a))
    count = 1
    for key in hashtable:
        stdio.writeln(str(count) + ": " + key.key + " " + str(hashtable.get(key.key)))
        count += 1

    stdio.writef("%d\n", hashtable.size())
    stdio.writeln("Get the: " + str(hashtable.get('thhhhhe')))
    stdio.writeln(hashtable.contains("thhhh"))

if __name__ == '__main__':
    main()
