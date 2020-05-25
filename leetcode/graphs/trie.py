# link: https://leetcode.com/problems/implement-trie-prefix-tree

# implement a trie daastrutcture or prefix datastructure
import collections
class TrieNode(object):
    def __init__(self):
        # Two things need to be defined here:
        # 1. children, where every children in itself is a Node
        # 2. Once the complete word is inserted, we wanna mark it as true or false
        #
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False


class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        current = self.root
        for letter in word:
            current = current.children[letter]
        current.is_word = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        current = self.root
        for letter in word:
            current = current.children.get(letter)
            if not current:
                return False
        return current.is_word

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """

        current = self.root
        for letter in prefix:
            current = current.children.get(letter)
            if not current:
                return False
        return True


if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple"))
    print(trie.search("app"))
    print(trie.startsWith("app"))
    print(trie.insert("app"))
    print(trie.search("app"))




