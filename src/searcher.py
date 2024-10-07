"""
This problem was asked by Twitter.

Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.
"""


class Searcher:
    def __init__(self, words: list[str]) -> None:
        self.words = words

    def search(self, q: str) -> list[str]:
        return list(filter(lambda w: w.startswith(q), self.words))

    def efficient_search(self, q: str) -> list[str]:
        return self.search(q)


class TrieNode:
    def __init__(self) -> None:
        self.children: dict[str, TrieNode] = {}
        self.is_end_of_word: bool = False


class Trie:
    def __init__(self) -> None:
        self.root: TrieNode = TrieNode()

    def insert(self, words: list[str]) -> None:
        for word in words:
            current = self.root
            for char in word:
                if char not in current.children:
                    current.children[char] = TrieNode()
                current = current.children[char]
            current.is_end_of_word = True

    def autocomplete(self, prefix: str) -> list[str]:
        current = self._search_prefix(prefix)
        if current is None:
            return []

        return self._find_words(current, prefix)

    def _search_prefix(self, prefix: str) -> TrieNode | None:
        current = self.root
        for char in prefix:
            if char not in current.children:
                return None
            current = current.children[char]
        return current

    def _find_words(self, node: TrieNode, prefix: str) -> list[str]:
        results = []
        if node.is_end_of_word:
            results.append(prefix)

        for char, child_node in node.children.items():
            more_results = self._find_words(child_node, prefix + char)
            results.append(*more_results)
        return results
