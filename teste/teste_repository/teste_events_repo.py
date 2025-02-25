from domeniu.entities import Event
from repository.event_repository import EventInMemoryRep
from utils.file_utils import clear_file_content, copy_file_content


def test_exists_with_id():
    test_repo = EventInMemoryRep()
    event1 = Event(1, '11/11', '11:11', 'nunta')
    event2 = Event(2, '11/12', '12:00', 'botez')
    test_repo.add(event1)
    test_repo.add(event2)

    assert test_repo.exists_with_id(1) is True
    assert test_repo.exists_with_id(5) is False


def test_find_event_id():
    test_repo = EventInMemoryRep()
    event1 = Event(55, '11/11', '11:11', 'nunta')
    event2 = Event(66, '11/12', '12:00', 'botez')
    test_repo.add(event1)
    test_repo.add(event2)
    assert test_repo.find_event__by_id(55) == event1
    assert test_repo.find_event__by_id(100) is None


def test_add_event():
    test_repo = EventInMemoryRep()
    event1 = Event(1, '11/11', '11:11', 'nunta')
    event2 = Event(2, '11/12', '12:00', 'botez')
    test_repo.add(event1)
    test_repo.add(event2)
    assert test_repo.get_lenght() == 2
    try:
        test_repo.add(event2)
        assert False
    except ValueError:
        assert True


def test_delete_event():
    test_repo = EventInMemoryRep()

    event1 = Event(1, '11/11', '11:11', 'nunta')
    event2 = Event(2, '11/12', '12:00', 'botez')
    test_repo.add(event1)
    test_repo.add(event2)
    assert test_repo.get_lenght() == 2

    test_repo.delete(1)
    assert test_repo.get_lenght() == 1
    assert test_repo.exists_with_id(1) is False


def test_get_lenght():
    test_repo = EventInMemoryRep()

    event1 = Event(1, '11/11', '11:11', 'nunta')
    event2 = Event(2, '11/12', '12:00', 'botez')
    test_repo.add(event1)
    test_repo.add(event2)
    assert test_repo.get_lenght() == 2


def test_find_event__by_id():
    test_repo = EventInMemoryRep()

    event1 = Event(1, '11/11', '11:11', 'nunta')
    event2 = Event(2, '11/12', '12:00', 'botez')
    test_repo.add(event1)
    test_repo.add(event2)
    assert test_repo.find_event__by_id(2) == event2
    assert test_repo.find_event__by_id(10) is None



def run_event_repo_tests():
    test_find_event_id()
    test_exists_with_id()
    test_add_event()
    test_delete_event()
    test_get_lenght()
    test_find_event__by_id()

