from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Driver(Base):
    __tablename__ = "drivers"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    document: Mapped[str] = mapped_column(String(255))
    client_id = mapped_column(ForeignKey("clients.id"))

    client: Mapped["Client"] = relationship(back_populates="drivers")
    telemetries: Mapped[list["Telemetry"]] = relationship(back_populates="driver")