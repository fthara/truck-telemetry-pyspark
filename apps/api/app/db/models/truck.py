from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Truck(Base):
    __tablename__ = "trucks"

    id: Mapped[int] = mapped_column(primary_key=True)
    license_plate: Mapped[str] = mapped_column(String(255))
    client_id = mapped_column(ForeignKey("clients.id"))

    client: Mapped["Client"] = relationship(back_populates="trucks")
    telemetries: Mapped[list["Telemetry"]] = relationship(back_populates="truck")