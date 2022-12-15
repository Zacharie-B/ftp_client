from entities.search import Search
import pytest


def test_create_search():
    search = Search([])
    assert search.get_key_words() == []


def test_store_search():
    search = Search(["ab", "bc", "cd"])
    assert search.get_key_words() == ["ab", "bc", "cd"]
