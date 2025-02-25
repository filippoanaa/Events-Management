import random
from random import randint

from domeniu.entities import *
from domeniu.validators import EventValidator


def random_string_generator(size, letters):
    return ''.join(random.choice(letters) for _ in range(size))


class EventController:
    def __init__(self, repository, validator: EventValidator):
        self.__repository = repository
        self.__validator = validator

    def add_event(self, event_id, date, time, description):
        """
        creeaza un eveniment si il valideaza
        :param event_id: int
        :param date: int
        :param time: int
        :param description: string
        :return: evenimentul creeat si validat
        """
        event = Event(event_id, date, time, description)
        self.__validator.validate_event(event)
        self.__repository.add(event)

    def delete_event(self, event_id):
        self.__repository.delete(event_id)

    def update_event(self, event_id, new_date, new_time, new_description):
        """
        creeaza un eveniment din datele introduse de utilizator, pe urma le valideaza
        :param event_id: int
        :param new_date: int
        :param new_time: int
        :param new_description: string
        :return:-
        """
        new_event = Event(event_id, new_date, new_time, new_description)
        self.__validator.validate_event(new_event)
        self.__repository.update(event_id, new_event)

    def find_event__by_id(self, id_to_search):
        return self.__repository.find_event__by_id(id_to_search)

    def get_all_events(self):
        return self.__repository.get_all()

    def add_event_random(self):
        event_id = randint(1, 50)
        date = random_string_generator(1, '0123') + random_string_generator(1,
                                                                            '123') + '/' + random_string_generator(
            1, '01') + random_string_generator(1, '12')
        time = random_string_generator(1, '01') + random_string_generator(1,
                                                                          '123456789') + ':' + random_string_generator(
            1, '01234') + random_string_generator(1, '012345')
        description = random_string_generator(10, 'abcdefghijklmnopqrstuvwxyz').capitalize()
        self.add_event(event_id, date, time, description)
