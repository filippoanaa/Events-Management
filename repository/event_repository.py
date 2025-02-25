from domeniu.entities import Event


class EventInMemoryRep:
    def __init__(self):
        self._events_list = []

    def find_index(self, event_id):
        """
        Returneaza pozitia(indexul) evenimentului din lista care are id-ul egal cu cel citit de la tastatura
        :param event_id: string, id-ul citit de la tastatura
        :return: index, int
        """
        for i, event in enumerate(self._events_list):
            if int(event.get_id()) == int(event_id):
                return i
        return -1

    def add(self, event):
        """
        Adauga un eveniment in lista de evenimente
        :param event object, obiect al clasei eveniment
        :return: -
               """
        if self.exists_with_id(event.get_id()):
            raise ValueError("Exista deja eveniment cu acest id!")
        self._events_list.append(event)

    def find_event__by_id(self, event_id):
        """
         Returneaza evenimentul din lista ce are id-ul egal cu cel citit de la tastatura
        :param event_id: string, id-ul evenimentului
        :return: eveniment, obiect al clasei eveniment
        """
        for event in self.get_all():
            if int(event.get_id()) == int(event_id):
                return event
        return None

    def exists_with_id(self, event_id):
        """
        Verifica daca exista in lista de evenimente un eveniment cu id-ul egal cu cel citit de la tastatura
        :param event_id: string ,id-ul citit de la tastatura
        :return: True daca se gaseste evenimentul, False altfrl
        :rtype: bool
         """
        for event in self.get_all():
            if event.get_id() == event_id:
                return True
        return False

    def update(self, event_id, new_event):
        """
        Modifica evenimentul cu id-ul citit (id_event) cu eveniemntul citit (event)
        :param event_id: int, id-ul evenimentului de modificat
        :param new_event: noul eveniment ce il va inlocui pe cel corespunzator
        :return: -
        """
        index = self.find_index(event_id)
        if id == -1:
            raise ValueError('Nu a fost gasit eveniment cu acest id')
        self._events_list[index] = new_event

    def delete(self, event_id):
        """
        Sterge evenimentul din lista care are id-ul egal cu cel citit de la tasattura
        :param event_id: string, id-ul evenimentului citit de la tastatura
        :return: -
        """
        new_events_list = []
        for event in self.get_all():
            if event.get_id() != event_id:
                new_events_list.append(event)
        self._events_list = new_events_list

    def get_all(self):
        return self._events_list

    def get_lenght(self):
        return len(self.get_all())


class EventFileRepo(EventInMemoryRep):
    def __init__(self, filename):
        EventInMemoryRep.__init__(self)
        self._filename = filename
        self.load_from_file()

    def load_from_file(self):
        all_events = []
        with open(self._filename, 'r') as f:
            lines = f.readlines()
            for line in lines:
                tokens = [token.strip() for token in line.split(';')]
                if len(tokens) == 3:
                    event_id, date, time, description = tokens
                    event = Event(event_id, date, time, description)
                    all_events.append(event)
        return all_events

    def save_to_file(self):
        events_list = EventInMemoryRep.get_all(self)
        with open(self._filename, 'w') as f:
            for event in events_list:
                event_str = str(event.get_id()) + ';' + str(event.get_date()) + ';' + str(
                    event.get_time()) + ';' + str(
                    event.get_description()) + '\n'
                f.write(event_str)

    def add(self, event):
        EventInMemoryRep.add(self, event)
        self.save_to_file()

    def get_all(self):
        return EventInMemoryRep.get_all(self)

    def delete(self, event_id):
        EventInMemoryRep.delete(self, event_id)
        self.save_to_file()

    def update(self, event_id, new_event):
        EventInMemoryRep.update(self, event_id, new_event)
        self.save_to_file()

    def find_index(self, event_id):
        return EventInMemoryRep.find_index(self, event_id)

    def find_event_by_id(self, event_id):
        return EventInMemoryRep.find_event__by_id(self, event_id)

    def exists_with_id(self, event_id):
        return EventInMemoryRep.exists_with_id(self, event_id)


