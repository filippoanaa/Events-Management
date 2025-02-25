from domeniu.entities import Person
from utils.sort_utils import cmp_persons, sort_persons_by_name


class PersonInMemoryRep:
    def __init__(self):
        self._persons_list = []

    def find_index(self, person_id):
        """
        returneaza pozitia persoanei din lista care are id-ul egal cu
        cel citit de la tastatura
        :param person_id: id citit
        :return: indexul
        """
        for i, person in enumerate(self.get_all()):
            if person.get_person_id() == person_id:
                return i
        return -1

    def find_person_by_id(self, person_id):
        """
        returneaza persoana care are id-ul egal cu cel citit de la tastatura
        :param person_id: id-ul citit de la tastaura
        :return: persoana
        """
        for person in self.get_all():
            if int(person.get_person_id()) == int(person_id):
                return person

        raise ValueError('Persoana cu id-ul dat nu exista in lista')

    def exists_with_id(self, person_id):
        """
         Verifica daca in lista curenta de persoane exista o persoana cu id-ul egal cu cel citit de la tastatura
         :param: id_citit- string, id-ul citit de la tastatura
        :return: True daca se gaseste o astfel de persoana, False altfel
         """
        for person in self.get_all():
            if person.get_person_id() == person_id:
                return True
        return False

    def add(self, person):
        """
        adauga o persoana
        :rtype: object
        :param person: persoana de adaugat
        :return: lista de persoane cu persoana person adaugata
        """
        if self.exists_with_id(person.get_person_id()):
            raise ValueError("Exista deja persoana cu acest id!")
        self._persons_list.append(person)

    def update(self, person_id, new_person):
        """
        Modifica persoana cu id-ul citit de la tastatura cu persoana noua citita de la tastatura
        :param person_id: id-ul persoanei
        :param new_person: object, obiect al clasei persoan
        :return: -
        """
        index = self.find_index(person_id)
        if index == -1:
            raise ValueError('Nu s a gasit persoana cu acest id')
        else:
            self._persons_list[index] = new_person

    def delete(self, person_id):
        """
        Sterge persoana cu id-ul dat din lista
        :param: person_id- int, id-ul persoanei ce trebuie eliminata din lista
        :return: -
        """
        new_persons_list = []
        for person in self.get_all():
            if person.get_person_id() != person_id:
                new_persons_list.append(person)
        self._persons_list = new_persons_list

    def get_all(self):
        """
        Returneaza lista de persoane
        :return: self.__persoans_list, lista de persoane
        """
        return self._persons_list

    def get_lenght(self):
        """
        lungimea listei de pers
        :return: lungimea listei
        """
        return len(self._persons_list)

    def persons_sorted_by_name(self):
        return sort_persons_by_name(self._persons_list)


class PersonFileRepo(PersonInMemoryRep):
    def __init__(self, filename):
        PersonInMemoryRep.__init__(self)
        self._filename = filename
        self.load_from_file()

    def load_from_file(self):
        all_persons = []
        with open(self._filename, 'r') as f:
            lines = f.readlines()
            for line in lines:
                tokens = [token.strip() for token in line.split(';')]
                if len(tokens) == 3:
                    person_id, name, address = tokens
                    person = Person(person_id, name, address)
                    all_persons.append(person)

        return all_persons

    def save_to_file(self):
        persons_list = PersonInMemoryRep.get_all(self)
        with open(self._filename, 'w') as f:
            for person in persons_list:
                person_str = str(person.get_person_id()) + ';' + str(person.get_name()) + ';' + str(
                    person.get_address()) + '\n'
                f.write(person_str)

    def get_all(self):
        return PersonInMemoryRep.get_all(self)

    def add(self, person):
        PersonInMemoryRep.add(self, person)
        self.save_to_file()

    def delete(self, person_id):
        PersonInMemoryRep.delete(self, person_id)
        self.save_to_file()

    def update(self, person_id, new_person):
        PersonInMemoryRep.update(self, person_id, new_person)
        self.save_to_file()

    def find_index(self, person_id):
        return PersonInMemoryRep.find_index(self, person_id)

    def exists_with_id(self, person_id):
        return PersonInMemoryRep.exists_with_id(self, person_id)

    def find_person_by_id(self, id_to_search):
        return PersonInMemoryRep.find_person_by_id(self, id_to_search)

    def persons_sorted_by_name(self):
        return PersonInMemoryRep.persons_sorted_by_name(self)
