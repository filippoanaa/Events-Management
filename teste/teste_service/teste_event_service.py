from domeniu.validators import EventValidator
from repository.event_repository import EventInMemoryRep
from service.event_service import EventController


def test_add_service():
    repo = EventInMemoryRep()
    validator = EventValidator()
    event_service = EventController(repo, validator)
    event_service.add_event(1, '11/11', '11:11', 'botez')
    assert len(event_service.get_all_events()) == 1
    try:
        event_service.add_event(1, '1111', '11vdf1', 'botez')
        assert False
    except ValueError:
        assert True


def test_delete_service():
    repo = EventInMemoryRep()
    validator = EventValidator()
    event_service = EventController(repo, validator)
    event_service.add_event(1, '11/11', '11:11', 'botez')
    assert len(event_service.get_all_events()) == 1
    event_service.delete_event(1)
    assert len(event_service.get_all_events()) == 0


def test_update_service():
    repo = EventInMemoryRep()
    validator = EventValidator()
    event_service = EventController(repo, validator)
    event_service.add_event(1, '11/11', '11:11', 'botez')
    event_service.update_event(1,'12/12', '12:12', 'nunta')
    new_event = event_service.find_event__by_id(1)
    assert new_event.get_date() == '12/12'
    assert new_event.get_description() == 'nunta'


def run_event_service_tests():
    test_add_service()
    test_delete_service()
    test_update_service()

