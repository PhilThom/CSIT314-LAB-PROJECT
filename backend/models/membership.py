from sqlalchemy import Column, Integer, String, Date
from ..database import Base


class Membership(Base):
    __tablename__ = "membership"

    id = Column(Integer, primary_key=True)
    client_id = Column(Integer)
    professional_id = Column(Integer)
    start_date = Column(Date)
    cost = Column(Integer)
    due_date = Column(Date)

    def __init__(self, id, client_id, professional_id, start_date, cost, due_date):
        self.id = id
        self.client_id = client_id
        self.professional_id = professional_id
        self.start_date = start_date
        self.cost = cost
        self.due_date = due_date

    def __repr__(self) -> str:
        return f"id={self.id}, client_id={self.client_id}, professional_id={self.professional_id}, start_date={self.start_date}, cost={self.cost}, due_date={self.due_date}"
