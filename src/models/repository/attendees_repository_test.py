import pytest
from src.models.settings.connection import db_connection_handler
from .attendees_repository import AttendeesRepository

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="Novo registro em banco de dados")
def test_insert_attendee():
    event_id = "teste-uuid-event"
    attendee_info = {
        "uuid": "teste-uuid-attendee",
        "name": "attendee name",
        "email": "attendee@domain.com",
        "event_id": event_id
    }
    attendee_repository = AttendeesRepository()
    response = attendee_repository.insert_attendee(attendee_info)
    print(response)

@pytest.mark.skip(reason="Nao necessario, apenas uma confirmacao/teste de integracao")
def test_get_attendee_badge_by_id():
    attendee_id = "teste-uuid-attendee"
    attendees_repository = AttendeesRepository()
    response = attendees_repository.get_attendee_badge_by_id(attendee_id)
    print(response)
    #print(response.title)