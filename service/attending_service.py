from domeniu.entities import Attending
from repository.attending_repository import AttendingInMemoryRep
from domeniu.validators import AttendingValidator
from repository.person_repository import PersonInMemoryRep
from repository.event_repository import EventInMemoryRep
from utils.sort_utils import selection_sort, shake_sort


class AttendingController:
    def __init__(self, repository: AttendingInMemoryRep, validator: AttendingValidator, repo1: PersonInMemoryRep,
                 repo2: EventInMemoryRep):
        self.__repository = repository
        self.__validator = validator
        self.__repo1 = repo1
        self.__repo2 = repo2

    def get_attending_list(self):
        return self.__repository.get_all()

    def add(self, person_id, event_id):
        attending = Attending(person_id, event_id)
        self.__validator.validate(attending)
        self.__repository.add(attending)

    def sorted_by_desc_date(self, person_id):
        person_events = []

        for att in self.__repository.get_all():
            if int(att.get_person_id()) == int(person_id):
                event_id = att.get_event_id()
                event = self.__repo2.find_event__by_id(event_id)
                person_events.append(event)
        return selection_sort(person_events, lambda e: (e.get_description(), e.get_date()))

    def persons_with_most_events(self):
        all_att = self.__repository.get_all()
        final = []
        for att in all_att:
            person_id = att.get_person_id()

            index = next((i for i, f in enumerate(final) if f.get_person_id() == person_id), None)

            if index is not None:
                final[index].inc_events()
            else:
                x = Attending(person_id, att.get_event_id())
                x.inc_events()
                final.append(x)

        for i in range(len(final)):
            x = self.__repo1.find_person_by_id(final[i].get_person_id())
            y = self.__repo2.find_event__by_id(final[i].get_event_id())
            final[i].set_name(x.get_name())
            final[i].set_description(y.get_description())
            final[i].set_address(x.get_address())

        s = selection_sort(final,lambda e: e.get_person_events(), reverse=True)
        return s[:len(s) // 2]

    def events_with_most_persons(self):
        all_att = self.__repository.get_all()
        final = []

        for att in all_att:
            event_id = att.get_event_id()
            index = next((i for i, f in enumerate(final) if f.get_event_id() == event_id), None)

            if index is not None:
                final[index].inc_persons()
            else:
                x = Attending(att.get_person_id(), event_id)
                x.inc_persons()
                final.append(x)

        for i in range(len(final)):
            x = self.__repo2.find_event__by_id(final[i].get_event_id())
            final[i].set_description(x.get_description())
        sort = shake_sort(final, lambda e: e.get_event_persons(), reverse=False)
        return sort
