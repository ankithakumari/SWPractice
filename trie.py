# Just the data structure
class TrieNode:

    def __init__(self):
        self.children = [None]*26
        self.isendofword = False
        self.childCount = 0



class Trie:
    def __init__(self):
        self.root = self.get_Node()

    def get_Node(self):
        return TrieNode()

    # return index based on input character
    def charToIndex(self, ch):
        return ord(ch) - ord('a')

    def insert(self, word):
        root_node = self.root
        n = len(word)
        for i in range(n):
            idx = self.charToIndex(word[i])

            if not root_node.children[idx]:
                root_node.children[idx] = self.get_Node()
            root_node.childCount += 1
            root_node = root_node.children[idx]

        root_node.isendofword = True

    def search(self, word):
        root_node = self.root
        n = len(word)
        for i in range(n):
            idx = self.charToIndex(word[i])
            if not root_node.children[idx]:
                return False
            root_node = root_node.children[idx]
        return root_node != None and root_node.isendofword

    def getUniquePrefix(self, word):
        root_node  = self.root
        n = len(word)
        for i in range(n):
            idx = self.charToIndex(word[i])
            root_node = root_node.children[idx]
            if root_node.childCount <= 1:
                return word[:i+1]



if __name__ == "__main__":
    wordList = ['zebra', 'dog', 'dove', 'duck']
    word_tree = Trie()
    for item in wordList:
        word_tree.insert(item)
    res = []
    for item in wordList:
        res.append(word_tree.getUniquePrefix(item))
    print(res)







