from src.models.settings.base import Base
from sqlalchemy import Column, String, DateTime, ForeignKey, Integer
from sqlalchemy.sql import func

class CheckIns(Base):
    __tablename__ = "check_ins"

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=func.now(), nullable=False)    
    attendeeId = Column(String, ForeignKey("attendees.id"), nullable=False)
    

    def __repr__(self):
        return f"CheckIns [attendees_id={self.attendees_id}]"

