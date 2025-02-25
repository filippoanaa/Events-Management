import random
import string

from domeniu.entities import Person


def random_string_generator(size, letters):
    return ''.join(random.choice(letters) for _ in range(size))


class PersonController:
    def __init__(self, repository, validator):
        self.__repository = repository
        self.__validator = validator

    def add_person(self, person_id, name, address):
        """
        creeaza persoana, valideaza datele introduse de utilizator despre persoana si adauga persoana in lista de pers
        :param person_id: int
        :param name: string
        :param address: string
        :return:obicetul persona
        """
        person = Person(person_id, name, address)
        self.__validator.validate_person(person)
        self.__repository.add(person)

    def delete_person(self, person_id):
        self.__repository.delete(person_id)

    def update_person(self, person_id, new_name, new_address):
        """
        modifica o persoana
        :param person_id: int
        :param new_name: string
        :param new_address: string
        :return: persoana modificata
        """
        new_person = Person(person_id, new_name, new_address)
        self.__validator.validate_person(new_person)
        self.__repository.update(person_id, new_person)

    def find_person_by_id(self, id_to_search):
        return self.__repository.find_person_by_id(id_to_search)

    def get_all_persons(self):
        return self.__repository.get_all()

    def add_person_random(self):
        person_id = random.randint(1, 50)
        name = random_string_generator(7,
                                       string.ascii_lowercase).capitalize() + ' ' + random_string_generator(7,
                                                                                                            string.ascii_lowercase).capitalize()
        address = random_string_generator(7,
                                         string.ascii_lowercase).capitalize() + ' ' + random_string_generator(
            10, string.ascii_lowercase).capitalize() + ',' + random_string_generator(3, string.digits)
        self.add_person(person_id, name, address)

    def persons_sorted_by_name(self):
        return self.__repository.persons_sorted_by_name()
