from domeniu.entities import Attending


class AttendingInMemoryRep:
    def __init__(self):
        self._attendings_list = []

    def add(self, attending):
        person_id = attending.get_person_id()
        event_id = attending.get_event_id()

        if self.find(person_id, event_id) is not None:
            raise ValueError('Legatura deja existenta!')
        self._attendings_list.append(attending)

    def find(self, id_person, id_event):
        for attending in self._attendings_list:
            if attending.get_person_id() == id_person and attending.get_event_id() == id_event:
                return attending
        return None

    def get_all(self):
        return self._attendings_list

    def get_length(self):
        return len(self._attendings_list)


class AttendingFileRepo(AttendingInMemoryRep):
    def __init__(self, filename):
        AttendingInMemoryRep.__init__(self)
        self.filename = filename
        self.load_from_file()

    def load_from_file(self):
        all_attendings = []
        with open(self.filename, 'r') as f:
            lines = f.readlines()
            for line in lines:
                person_id, event_id = [token.strip() for token in line.split(';')]
                attending = Attending(person_id, event_id)
                all_attendings.append(attending)
        return all_attendings

    def save_to_file(self):
        attendings_list = AttendingFileRepo.get_all(self)
        with open(self.filename, 'w') as f:
            for att in attendings_list:
                att_str = str(att.get_person_id()) + ';' + str(att.get_event_id()) + '\n'
                f.write(att_str)

    def add(self, attending):
        AttendingInMemoryRep.add(self, attending)
        self.save_to_file()

    def get_all(self):
        return AttendingInMemoryRep.get_all(self)

    def get_length(self):
        return AttendingInMemoryRep.get_length(self)
