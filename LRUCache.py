# LRUCache class defines all the methods of LRU: get,put,delete and reset
import collections


class LRUCache:
    # __init__(self,capacity) defines the cache_table as ordered Dictionary with size = capacity
    # order of the dictionary will be according to FIFO First In First Out order
    def __init__(self, capacity):
        self.cache_table = collections.OrderedDict()
        self.capacity = capacity

    # get(self,key) will look into the cache_table and check whether the key is available or not.
    # If the key is found in the cache_table, get the value, pop that item and add it to the OrderedDictionary
    # Else return None
    def get(self, key):
        if key not in self.cache_table:
            return None
        value = self.cache_table.pop(key)
        self.cache_table[key] = value
        return value

    # put(self,key,value) will check whether the key is present in the cache_table or not
    # If key is present, pop that item and add it to the OrderedDictionary
    # Else if key is not present and the capacity of OrderedDictionary is full, then pop the least recently used item
    # i.e. the last item form the orderedDictionary following FIFO order
    # And then add the new key, value pair to the OrderedDictionary
    def put(self, key, value):
        if key in self.cache_table:
            value = self.cache_table.pop(key)
        elif self.capacity <= len(self.cache_table):
            self.cache_table.popitem(last=False)  # last = False for FIFO order
        self.cache_table[key] = value

    # delete(self,key) will pop the item from the OrderedDictionary if key is present in it
    def delete(self, key):
        if key in self.cache_table:
            self.cache_table.pop(key)

    # reset(self) will remove all the items from ordered cache
    def reset(self):
        self.cache_table.clear()


if __name__ == '__main__':
    print("Initializing LRU cache with max sixe : 3")
    lru = LRUCache(3)
    print("Put key=1 and value= Apple")
    lru.put(1,"Apple")
    print("Cache table: ",lru.cache_table)
    print("Put key=2 and value= Banana")
    lru.put(2,"Banana")
    print("Cache table: ", lru.cache_table)
    print("Put key=3 and value= Mango")
    lru.put(3,"Mango")
    print("Cache table: ", lru.cache_table)
    print("Get value for key=4")
    value = lru.get(4)
    print("Value =",value)
    print("Cache table: ", lru.cache_table)
    print("Put key=2 and value= Banana")
    lru.put(2,"Banana")
    print("Cache table: ", lru.cache_table)
    print("Get value for key=1")
    value = lru.get(1)
    print("Value=",value)
    print("Cache table: ", lru.cache_table)
    print("Put key=4 and value= Guava")
    lru.put(4,"Guava")
    print("Cache table: ", lru.cache_table)
    print("Delete key=2")
    lru.delete(2)
    print("Cache table: ", lru.cache_table)
    print("Reset LRUCache")
    lru.reset()
    print("Cache table: ", lru.cache_table)