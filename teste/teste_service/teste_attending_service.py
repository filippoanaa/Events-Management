from repository.person_repository import PersonInMemoryRep
from repository.event_repository import EventInMemoryRep
from repository.attending_repository import AttendingInMemoryRep
from domeniu.validators import AttendingValidator
from service.attending_service import AttendingController
from domeniu.entities import Person, Event


def test_add_attending():
    repo_person = PersonInMemoryRep()
    repo_event = EventInMemoryRep()
    person1 = Person(1, 'Ana Filip', 'strada princupala, nr 1')
    event1 = Event(1, '11/11', '11:11', 'nunta')
    repo_person.add(person1)
    repo_event.add(event1)

    repo_attending = AttendingInMemoryRep()
    attending_validator = AttendingValidator()
    attending_controller = AttendingController(repo_attending, attending_validator, repo_person, repo_event)
    attending_controller.add(1, 1)

    assert len(repo_attending.get_all()) == 1


def test_sorted_by_desc_date():
    repo_person = PersonInMemoryRep()
    repo_event = EventInMemoryRep()
    attending_validator = AttendingValidator()
    repo_attending = AttendingInMemoryRep()
    attending_controller = AttendingController(repo_attending, attending_validator, repo_person, repo_event)
    assert attending_controller.sorted_by_desc_date(106) == []


def run_attending_service_tests():
    test_add_attending()
    test_sorted_by_desc_date()
