class TrieNode():
    def __init__(self):
        self.children = {}
        self.last = False


class Trie():
    def __init__(self):
        self.root = TrieNode()
        self.word_list = []

    def formTrie(self, keys):
        for key in keys:
            self.insert(key)

    def insert(self, key):
        node = self.root
        for a in list(key):
            if not node.children.get(a):
                node.children[a] = TrieNode()

            node = node.children[a]
        node.last = True

    def search(self, key):
        node = self.root
        found = True

        for a in list(key):
            if not node.children.get(a):
                found = False
                break

            node = node.children[a]
        return node and node.last and found

    def suggestionsRec(self, node, word):
        if node.last:
            self.word_list.append(word)

        for a, n in node.children.items():
            self.suggestionsRec(n, word + a)

    def printAutoSuggestions(self, key):
        node = self.root
        not_found = False
        temp_word = ''

        for a in list(key):
            if not node.children.get(a):
                not_found = True
                break

            temp_word += a
            node = node.children[a]

        if not_found:
            return 0
        elif node.last and not node.children:
            return -1

        self.suggestionsRec(node, temp_word)
        print(' '.join(self.word_list[:3]))

        if len(self.word_list) >= 3:
            return self.word_list[:3]
        return self.word_list


def threeProductSuggestions(numProducts, repository, customerQuery):
    repository.sort()
    result = []
    for i in range(4, len(customerQuery) + 1):
        t = Trie()
        t.formTrie(repository)
        res = t.printAutoSuggestions(customerQuery[:i])
        result.append(res)
    return result


numProducts = 5
repository = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]  # keys to form the trie structure.
customerQuery = "mouse"
threeProductSuggestions(5, repository, customerQuery)
