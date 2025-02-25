from domeniu.validators import EventValidator
from repository.event_repository import EventFileRepo
from service.event_service import EventController
from UI.console import Console

from domeniu.validators import PersonValidator
from repository.person_repository import PersonFileRepo
from service.person_service import PersonController

from domeniu.validators import AttendingValidator
from service.attending_service import AttendingController
from repository.attending_repository import AttendingFileRepo

from teste.teste_domeniu.teste_validatori import validators_tests
from teste.teste_domeniu.teste_entitati import run_entities_tests

from teste.teste_repository.teste_events_repo import run_event_repo_tests
from teste.teste_repository.teste_person_repo import run_person_repo_tests
from teste.teste_repository.teste_attending_repo import run_attending_repo_tests

from teste.teste_service.teste_person_service import run_person_service_tests
from teste.teste_service.teste_event_service import run_event_service_tests
from teste.teste_service.teste_attending_service import run_attending_service_tests
if __name__ == '__main__':
    repo1 = PersonFileRepo('utils/persons.txt')
    val1 = PersonValidator()
    srv1 = PersonController(repo1, val1)

    repo2 = EventFileRepo('utils/events.txt')
    val2 = EventValidator()
    srv2 = EventController(repo2, val2)

    repo3 = AttendingFileRepo('utils/attendings.txt')
    val3 = AttendingValidator()
    srv3 = AttendingController(repo3, val3, repo1, repo2)
    console = Console(srv1, srv2, srv3)

    ui = Console(srv1, srv2, srv3)

    run_entities_tests()
    validators_tests()
    run_event_repo_tests()
    run_person_repo_tests()
    run_attending_repo_tests()
    run_entities_tests()
    run_person_service_tests()
    run_event_service_tests()
    run_attending_service_tests()
    ui.run()


