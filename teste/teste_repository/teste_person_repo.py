from domeniu.entities import Person
from repository.person_repository import PersonInMemoryRep
from utils.file_utils import copy_file_content, clear_file_content


def test_add():
    test_repo = PersonInMemoryRep()
    person1 = Person(1, 'Ana Filip', 'str Principala, nr 1')
    person2 = Person(2, 'Robert Pop', 'strada emil garleanu, nr 19')
    test_repo.add(person1)
    test_repo.add(person2)
    assert test_repo.get_lenght() == 2
    try:
        test_repo.add(person2)
        assert False
    except ValueError:
        assert True


def test_exists_with_id():
    test_repo = PersonInMemoryRep()
    person1 = Person(1, 'Ana Filip', 'str Principala, nr 1')
    person2 = Person(2, 'Robert Pop', 'strada emil garleanu, nr 19')
    test_repo.add(person1)
    test_repo.add(person2)
    assert test_repo.exists_with_id(1) is True
    assert test_repo.exists_with_id(3) is False


def test_find_person_by_id():
    test_repo = PersonInMemoryRep()
    person1 = Person(1, 'Ana Filip', 'str Principala, nr 1')
    person2 = Person(2, 'Robert Pop', 'strada emil garleanu, nr 19')
    test_repo.add(person1)
    test_repo.add(person2)
    assert test_repo.find_person_by_id(2) == person2
    try:
        test_repo.find_person_by_id(4)
        assert False
    except ValueError:
        assert True


def test_find_index():
    test_repo = PersonInMemoryRep()
    person1 = Person(1, 'Ana Filip', 'str Principala, nr 1')
    person2 = Person(2, 'Robert Pop', 'strada emil garleanu, nr 19')
    test_repo.add(person1)
    test_repo.add(person2)
    assert test_repo.find_index(2) == 1
    assert test_repo.find_index(5) == -1


def test_delete_person():
    test_repo = PersonInMemoryRep()
    person1 = Person(1, 'Ana Filip', 'str Principala, nr 1')
    person2 = Person(2, 'Robert Pop', 'strada emil garleanu, nr 19')
    test_repo.add(person1)
    test_repo.add(person2)
    assert test_repo.get_lenght() == 2
    test_repo.delete(2)
    assert test_repo.get_lenght() == 1
    assert test_repo.exists_with_id(1) is True


def test_get_lenght():
    test_repo = PersonInMemoryRep()
    person1 = Person(1, 'Ana Filip', 'str Principala, nr 1')
    person2 = Person(2, 'Robert Pop', 'strada emil garleanu, nr 19')
    test_repo.add(person1)
    test_repo.add(person2)
    assert test_repo.get_lenght() == 2


def run_person_repo_tests():
    test_find_person_by_id()
    test_exists_with_id()
    test_find_index()
    test_delete_person()
    test_get_lenght()
    test_add()
