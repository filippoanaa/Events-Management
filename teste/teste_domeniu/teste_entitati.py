from domeniu.entities import Event, Person, Attending


def test_create_person():
    person1 = Person(1, 'Anca Filip', 'strada lalelelor, nr 12')
    assert person1.get_name() == 'Anca Filip'
    person1.set_name('Anca Hertia')
    assert person1.get_name() == 'Anca Hertia'


def test_create_event():
    event1 = Event(1, '11/11', '11:11', 'nunta')
    assert event1.get_time() == '11:11'
    assert event1.get_date() == '11/11'
    assert event1.get_description() == 'nunta'


def test_link_entity():
    entity = Attending(1, 5)
    assert entity.get_person_id() == 1
    assert entity.get_event_id() == 5


def run_entities_tests():
    test_create_person()
    test_create_event()
    test_link_entity()
