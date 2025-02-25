def is_str(msg):
    """
    verifica daca mesajul dat este string
    :param msg: mesajul de verificat
    :return:true/false
    """
    try:
        return isinstance(msg, str)
    except ValueError:
        return False


class PersonValidator:
    def validate_person(self, person):
        """
    Valideaza o persoana
    :param person: persoana care se valideaza
    :return: -
    :raises: ValueError daca persoana nu e valida
    """

        errors = []

        if len(person.get_name().split()) < 2 or len(person.get_name().split()) > 2:
            errors.append("Numele persoanei trebuie sa aiba exact 2 cuvinte! ")
        if len(person.get_address().split(",")) < 2:
            errors.append("Adresa persoanei trebuie sa aiba o strada si un numar!")

        if len(errors) != 0:
            error_string = '\n'.join(errors)
            raise ValueError(error_string)


def valid_date(date):
    date_list = date.split("/")
    errors = []

    if len(date_list) != 2:
        errors.append("Data nu a fost introdusă corect. Trebuie să conțină o zi și o lună")
    else:
        day = date_list[0].strip()
        month = date_list[1].strip()

        if not day.isdigit():
            errors.append("Ziua trebuie să fie nr întreg")
        elif int(day) < 1 or int(day) > 31:
            errors.append("Ziua trebuie să fie cuprinsă între 1 și 31")

        if not month.isdigit():
            errors.append("Luna trebuie să fie nr întreg")
        elif int(month) < 1 or int(month) > 12:
            errors.append("Luna trebuie să fie cuprinsă între 1 și 12")

    return errors


def valid_time(time):
    time_list = time.split(":")
    errors = []

    if len(time_list) != 2:
        errors.append("Timpul trebuie să conțină ora și minutele")
    else:
        hour = time_list[0].strip()
        minutes = time_list[1].strip()

        if not hour.isdigit():
            errors.append("Ora trebuie să fie număr întreg")
        elif int(hour) < 0 or int(hour) > 23:
            errors.append("Ora trebuie să fie între 0 și 23")

        if not minutes.isdigit():
            errors.append("Minutele trebuie să fie număr întreg")
        elif int(minutes) < 0 or int(minutes) > 59:
            errors.append("Minutele trebuie să fie între 0 și 59")

    return errors


class EventValidator:

    def validate_event(self, event):
        errors = []
        date_errors = valid_date(event.get_date())
        time_errors = valid_time(event.get_time())
        for er in date_errors:
            errors.append(er)
        for er in time_errors:
            errors.append(er)
        if event.get_description() == "":
            errors.append("Descriere evenimentului trebuie sa existe")

        if len(errors) > 0:
            error_string = '\n'.join(errors)
            raise ValueError(error_string)


class AttendingValidator:
    def validate(self, attending):
        errors_list = []
        if int(attending.get_person_id() is None):
            errors_list.append('Id-ul persoanei trebuie sa existe')
        if int(attending.get_event_id() is None):
            errors_list.append('Id-ul evenimentului trenuie sa existe')

        if len(errors_list) > 0:
            error_string = '\n'.join(errors_list)
            raise ValueError(error_string)
