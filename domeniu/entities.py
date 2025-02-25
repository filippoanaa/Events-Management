class Event:
    def __init__(self, event_id, date, time, description):
        self.__event_id = event_id
        self.__date = date
        self.__time = time
        self.__description = description

    def get_id(self):
        return self.__event_id

    def get_date(self):
        return self.__date

    def get_time(self):
        return self.__time

    def get_description(self):
        return self.__description

    def set_id(self, new_id):
        self.__event_id = new_id

    def set_date(self, new_date):
        self.__description = new_date

    def set_time(self, new_time):
        self.__time = new_time

    def set_description(self, new_description):
        self.__description = new_description

    def __repr__(self):
        return "Id:" + str(self.__event_id) + ' ' + "Date:" + str(self.__date) + ' ' + "Time:" + str(
            self.__time) + ' ' + 'Descriere:' + str(self.__description)


class Person:
    def __init__(self, person_id, name, address):
        self.__person_id = person_id
        self.__name = name
        self.__address = address

    def get_person_id(self):
        return self.__person_id

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def set_id(self, new_person_id):
        self.__person_id = new_person_id

    def set_name(self, new_name):
        self.__name = new_name

    def set_address(self, new_address):
        self.__address = new_address

    def __repr__(self):
        return "Id:" + str(self.__person_id) + ' ' + "Name:" + str(self.__name) + ' ' + " address:" + str(self.__address)


class Attending:
    def __init__(self, person_id, event_id):
        self.__person_id = person_id
        self.__event_id = event_id
        self.__address = ''
        self.__name = ""
        self.__description = ""
        self.__date = ""
        self.__description = ""

        self.__person_events = 0
        self.__event_persons = 0

    def get_person_id(self):
        return self.__person_id

    def get_event_id(self):
        return self.__event_id

    def get_person_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_date(self):
        return self.__date

    def get_description(self):
        return self.__description

    def get_person_events(self):
        return self.__person_events

    def get_event_persons(self):
        return self.__event_persons

    def set_name(self, new_name):
        self.__name = new_name

    def set_address(self, address):
        self.__address = address

    def set_date(self, new_date):
        self.__date = new_date

    def set_description(self, new_description):
        self.__description = new_description

    def inc_events(self):
        self.__person_events += 1

    def inc_persons(self):
        self.__event_persons += 1

    def __str__(self):
        return 'Persoana: ' + str(self.__person_id) + ' ' + 'participa la evenimentul cu id-ul: ' + ' ' + str(
            self.__event_id)
