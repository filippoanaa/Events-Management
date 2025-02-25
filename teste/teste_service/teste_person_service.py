from domeniu.validators import PersonValidator
from repository.person_repository import PersonInMemoryRep
from service.person_service import PersonController


def test_add_service():
    repo = PersonInMemoryRep()
    validator = PersonValidator()
    person_service = PersonController(repo, validator)
    person_service.add_person(1, 'Ana Filip', 'strada principala, nr 1')
    assert len(person_service.get_all_persons()) == 1
    try:
        person_service.add_person(1, 'Ana Filip', 'strada principala, nr 1')
        assert False
    except ValueError:
        assert True


def test_delete_service():
    repo = PersonInMemoryRep()
    validator = PersonValidator()
    person_service = PersonController(repo, validator)
    person_service.add_person(1, 'Ana Filip', 'strada principala, nr 1')
    assert len(person_service.get_all_persons()) == 1
    person_service.delete_person(100)
    assert len(person_service.get_all_persons()) == 1
    person_service.delete_person(1)
    assert len(person_service.get_all_persons()) == 0


def test_update_service():
    repo = PersonInMemoryRep()
    validator = PersonValidator()
    person_service = PersonController(repo, validator)
    person_service.add_person(1, 'Ana Filip', 'strada principala, nr 1')
    person_service.update_person(1, 'nume nou', 'adresa noua, nr nou')
    new_person = person_service.find_person_by_id(1)
    assert new_person.get_name() == 'nume nou'
    assert new_person.get_address() == 'adresa noua, nr nou'
    try:
        person_service.update_person(1, 'efg', 'wdf')
        assert False
    except ValueError:
        assert True


def run_person_service_tests():
    test_add_service()
    test_delete_service()
    test_update_service()
