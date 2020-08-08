# link: https://leetcode.com/problems/design-hashset/submissions/

class ListNode(object):
    def __init__(self, key):
        self.key = key
        self.next = None

class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.bucket_size = 1000000;
        self.bucket = [None]* self.bucket_size
        

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key == 0:
            index = 0
        else:
            index = self.bucket_size%key
        
        if not self.bucket[index]:
            self.bucket[index] = ListNode(key)
        else:
            current = self.bucket[index]
            while True:
                # current = current.next
                if current.key == key:
                    return
                if not current.next:
                    break
                current = current.next
            current.next = ListNode(key)
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key == 0:
            index = 0
        else:
            index = self.bucket_size%key
        curr = prev = self.bucket[index]
        if not curr:
            return False
        if curr.key == key:
            self.bucket[index] = curr.next
        else:
            curr = curr.next
            while curr:
                if curr.key == key:
                    prev.next = curr.next
                    break
                else:
                    curr = curr.next
                    prev = prev.next
                    
                    
                    
            
        
        

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        if key == 0:
            index = 0
        else:
            index = self.bucket_size%key
        curr = self.bucket[index]
        if not curr:
            return False
        else:
            while curr:
                if curr.key == key:
                    return True
                curr = curr.next
        return False
                    
        
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)