"""
We want to implement search, particularly as it relates to finding keywords in a database.

We should implement a trie (prefix tree) data structure.

We should implement methods for insert and find words.

Discuss time and space complexity.
"""

class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.is_end_of_word = False

# insertion O(m) where m = length of the word
# search O(m) for a word or prefix of length m

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
    
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word
    
    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
    
"""
example trie with 'cat', 'cow', and 'to'
            [*]
    [c]             [t]
[a]     [o]         [o]
[t]     [w]

"""

# usage
trie = Trie()
words = ['apple', 'application', 'banana']
for word in words:
    trie.insert(word)

print(trie.search("apple"))  # True
print(trie.search("appl"))   # False
print(trie.starts_with("app"))  # True
print(trie.starts_with("ban"))  # True
print(trie.starts_with("cat"))  # False