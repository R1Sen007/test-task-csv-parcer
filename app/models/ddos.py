from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Float

from app.core.db import Base


class Ddos(Base):
    '''
    Model for info about ddos.
    '''

    saddr: Mapped[str] = mapped_column(String, primary_key=True)
    avgDur: Mapped[float] = mapped_column(Float)
