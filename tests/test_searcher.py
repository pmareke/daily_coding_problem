import pytest
from expects import equal, expect

from src.searcher import Searcher, Trie

"""
This problem was asked by Twitter.

Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.
"""


class TestSearcher:
    @pytest.mark.parametrize(
        "words,q,expected",
        [
            (["a", "b", "c"], "x", []),
            (["blue", "blur"], "blu", ["blue", "blur"]),
            (["dog", "deer", "deal"], "de", ["deer", "deal"]),
        ],
    )
    def test_search(self, words: list[str], q: str, expected: list[str]) -> None:
        searcher = Searcher(words)

        found_words = searcher.search(q)

        expect(found_words).to(equal(expected))

    @pytest.mark.parametrize(
        "words,q,expected",
        [
            (["a", "b", "c"], "x", []),
            (["blue", "blur"], "blu", ["blue", "blur"]),
            (["dog", "deer", "deal"], "de", ["deer", "deal"]),
        ],
    )
    def test_efficiente_search(
        self, words: list[str], q: str, expected: list[str]
    ) -> None:
        trie = Trie()
        trie.insert(words)

        found_words = trie.autocomplete(q)

        expect(found_words).to(equal(expected))
