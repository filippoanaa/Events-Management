def print_menu():
    print("\nPP.Printeaza lista de persoane ")
    print("PE.Printeaza lista de evenimente")
    print('PA.Printeaza lista de participari')
    print("1.Aduaga  persoana")
    print("2.Adauga eveniment")
    print("3.Sterge persoana")
    print("4.Sterge eveniment")
    print("5.Modifica persoana")
    print("6.Modifica eveniment")
    print('7.Cauta persoana')
    print('8.Cauta eveniment')
    print('9.Adauga persoana la eveniment')
    print('10.Adauga persoana random.')
    print('11.Adauga eveniment random')
    print('12.Lista de evenimente la care participă o persoană ordonata alfabetic după descriere')
    print('13.Persoane participante la cele mai multe evenimente')
    print('14.Primele 20% evenimente cu cei mai mulți participanți (descriere, număr participanți')
    print('15.Persoane sortate dupa nume')


class Console:
    def __init__(self, person_service, event_service, attenting_service):
        self.__person_service = person_service
        self.__event_service = event_service
        self.__attending_service = attenting_service

    def print_persons_list(self):
        for person in self.__person_service.get_all_persons():
            print(person)

    def print_events_list(self):
        for event in self.__event_service.get_all_events():
            print(event)

    def print_attendings_list(self):
        for att in self.__attending_service.get_attending_list():
            print(att)

    def ui_add_person(self):
        person_id = input('ID: ')
        name = input('Nume complet(nume + prenume): ')
        address = input('Adresa completa(strada, nr): ')
        try:
            self.__person_service.add_person(person_id, name, address)
            print('Persoana a fost adaugata cu succes!')
        except ValueError as ve:
            print(ve)

    def ui_add_event(self):
        event_id = input("Id: ")
        date = input("Data(zi/luna): ")
        time = input("Ora: ")
        description = input("Descrierea: ")
        try:
            self.__event_service.add_event(event_id, date, time, description)
            print('Evenimentul a fost adaugat cu succes!')
        except ValueError as ve:
            print(ve)

    def ui_delete_person(self):
        person_id = input('ID-ul personei pe care doriti sa o stergeti:')
        try:
            self.__person_service.delete_person(person_id)
            print('Persoana a fost stearsa cu succes!')
        except ValueError as ve:
            print(ve)

    def ui_delte_event(self):
        event_id = input("ID-ul evenimentului pe care doriti sa il stergeti: ")
        try:
            self.__event_service.delete_event(event_id)
            print('Evenimentul a fost sters cu succes!')
        except ValueError as ve:
            print(ve)

    def ui_update_person(self):
        person_id = input('Introduceti id-ul persoanei pe care doriti sa o modificati: ')
        new_name = input('Nume nou: ')
        new_address = input('Adresa noua: ')
        try:
            self.__person_service.update_person(person_id, new_name, new_address)
            print('Persoana a fost modificata cu succes!')
        except ValueError as ve:
            print(ve)

    def ui_update_event(self):
        event_id = input('Introduceti id-ul evenimentului pe care doriti sa il modificati: ')
        new_date = input('Data noua: ')
        new_time = input('Ora noua: ')
        new_description = input('Noua descriere: ')
        try:
            self.__event_service.update_event(event_id, new_date, new_time, new_description)
            print('Evenimentul a fost modificat cu succes!')
        except ValueError as ve:
            print(ve)

    def ui_search_person(self):
        id_to_search = input('Introduceti ID-ul persoanei pe care sa o cautam: ')
        try:
            print(self.__person_service.find_person_by_id(id_to_search))
        except ValueError as ve:
            print(ve)

    def ui_find_event__by_id(self):
        id_to_search = input('Introduceti id-ul evenimentului: ')
        try:
            print(self.__event_service.find_event__by_id(id_to_search))
        except ValueError as ve:
            print(ve)

    def ui_add_person_to_event(self):
        person_id = input('Introduceti id-ul persoanei: ')
        event_id = input('Introduceti id-ul evenimentului: ')
        try:
            self.__attending_service.add(person_id, event_id)
            print('Legatura a fost creeata cu succes!')
        except ValueError as ve:
            print(ve)

    def ui_add_event_random(self):
        try:
            self.__event_service.add_event_random()
        except ValueError as ve:
            print(ve)

    def ui_add_person_random(self):
        try:
            self.__person_service.add_person_random()
        except ValueError as ve:
            print(ve)

    def ui_sorted_by_desc_date(self):
        person_id = input('Introduceti id-ul persoanei:')
        try:
            sorted_persons = self.__attending_service.sorted_by_desc_date(person_id)
            for s in sorted_persons:
                print(s.get_description(), ',', s.get_date())

        except ValueError as ve:
            print(ve)

    def ui_persons_with_most_events(self):
        try:
            bussiest_persons = self.__attending_service.persons_with_most_events()
            for person in bussiest_persons:
                print(person.get_person_name(), ',', person.get_address(), ':', person.get_person_events())
        except ValueError as ve:
            print(ve)

    def ui_events_with_most_people(self):
        try:
            events = self.__attending_service.events_with_most_persons()
            for e in events:
                print(e.get_description(), ':', e.get_event_persons())
        except ValueError as ve:
            print(ve)

    def ui_persons_sorted_by_name(self):
        try:
            persons = self.__person_service.persons_sorted_by_name()
            for p in persons:
                print(p)
        except ValueError as ve:
            print(ve)

    def run(self):
        while True:
            print_menu()
            cmd = input("Introduceti optiunea dvs: ")
            cmd = cmd.upper().strip()
            if cmd == 'PP':
                self.print_persons_list()
            if cmd == 'PE':
                self.print_events_list()
            if cmd == 'PA':
                self.print_attendings_list()
            if cmd == '1':
                self.ui_add_person()
            if cmd == '2':
                self.ui_add_event()
            if cmd == '3':
                self.ui_delete_person()
            if cmd == '4':
                self.ui_delte_event()
            if cmd == '5':
                self.ui_update_person()
            if cmd == '6':
                self.ui_update_event()
            if cmd == '7':
                self.ui_search_person()
            if cmd == '8':
                self.ui_find_event__by_id()
            if cmd == '9':
                self.ui_add_person_to_event()
            if cmd == '10':
                self.ui_add_person_random()
            if cmd == '11':
                self.ui_add_event_random()
            if cmd == '12':
                self.ui_sorted_by_desc_date()
            if cmd == '13':
                self.ui_persons_with_most_events()
            if cmd == '14':
                self.ui_events_with_most_people()
            if cmd == '15':
                self.ui_persons_sorted_by_name()
