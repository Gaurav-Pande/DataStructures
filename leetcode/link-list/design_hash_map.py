# link: https://leetcode.com/problems/design-hashmap/

class ListNode(object):
    def __init__(self, key, val):
        self.value = (key, val)
        self.next = None
        
        
class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.bucket_size = 1000
        self.bucket = [None]*self.bucket_size
        

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        index =key%self.bucket_size
        if not self.bucket[index]:
            self.bucket[index] = ListNode(key, value)
        else:
            current = self.bucket[index]
            while True:
                if current.value[0] == key:
                    current.value = (key,value)
                    return
                if not current.next:
                    break
                current = current.next
            current.next = ListNode(key,value)
                    
                
        
        
        

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        index = key%self.bucket_size
        current = self.bucket[index]
        while current:
            if current.value[0]==key:
                return current.value[1]
            else:
                current = current.next
        return -1
            
        
        

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        index = key % self.bucket_size
        # 2 pointers needs to be taken here
        current = prev = self.bucket[index]
        if not current:
            return
        if current.value[0]==key:
            self.bucket[index]= current.next
        else:
            current = current.next
            while current:
                if current.value[0] == key:
                    prev.next = current.next
                    break
                else:
                    current = current.next
                    prev = prev.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)