import random


class RandomizedSet(object):

    def __init__(self):
        self.collection = {}
        self.listArray = []

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.collection:
            self.collection[val] = len(self.listArray)
            self.listArray.append(val)
            return True
        else:
            return False

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.collection:
            return False
        else:
            idx = self.collection[val]
            lastVal = self.listArray[-1]
            self.listArray[idx] = lastVal
            self.listArray.pop()
            self.collection[lastVal] = idx
            del self.collection[val]
            return True

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.listArray)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()