from entities.search_cache import SearchCache
from entities.search import Search
import pytest

sc = SearchCache()


def test_create_search_cache():
    assert sc.get_searches() == []


def test_add():
    s1 = Search(['pdf', 'docx'])
    s2 = Search(['xml', 'txt'])
    sc.add(s1)
    sc.add(s2)
    assert sc.get_searches()[0] == s2
    assert sc.get_searches()[1] == s1


def test_remove_all():
    sc.add(Search(['pdf', 'docx']))
    sc.add(Search(['xml', 'txt']))
    assert len(sc.get_searches()) >= 1
    sc.remove_all()
    assert len(sc.get_searches()) == 0


def test___str__():
    sc.add(Search(['pdf', 'docx']))
    sc.add(Search(['xml', 'txt']))
    string = "Your previous searches are :"
    for search in sc.get_searches():
        string += "\n" + search.get_key_words()[0] + " " + search.get_key_words()[1] + " "
    assert string == sc.__str__()
