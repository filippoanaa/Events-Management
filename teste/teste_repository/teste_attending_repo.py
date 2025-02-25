from repository.attending_repository import AttendingInMemoryRep
from domeniu.entities import Attending, Event, Person


def test_add():
    repo_test = AttendingInMemoryRep()
    event1 = Event(1, '11/11', '11:11', 'nunta')
    person1 = Person(1, 'Ana Filip', 'str Principala, nr 1')
    link1 = Attending(person1.get_person_id(), event1.get_id())
    assert repo_test.get_length() == 0
    repo_test.add(link1)
    assert repo_test.get_length() == 1
    try:
        repo_test.add(link1)
        assert False
    except ValueError:
        assert True


def test_find():
    repo_test = AttendingInMemoryRep()
    event1 = Event(1, '11/11', '11:11', 'nunta')
    person1 = Person(1, 'Ana Filip', 'str Principala, nr 1')
    link1 = Attending(person1.get_person_id(), event1.get_id())
    repo_test.add(link1)
    assert repo_test.find(1, 1) == link1
    assert repo_test.find(1, 3) is None


def run_attending_repo_tests():
    test_add()
    test_find()

